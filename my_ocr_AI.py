import os
import time
import json
import re
import openpyxl
from PIL import Image
from google import genai
from google.genai import types

# ========================================================
# [설정] API 키를 입력하세요
GOOGLE_API_KEY = "AIzaSyBIPVSTKrVRi7OfClHFJlTXDTxfNJls3J4"

# 경로
image_folder = r"C:\Users\qeem\python\사진"
template_path = r"C:\Users\qeem\python\사진\차량명세서 샘플.xlsx"
START_ROW = 5
# ========================================================

def run_alias_mode():
    print("--- 🚀 Gemini 1.5 별칭(Alias) 모드 시작 ---")
    
    try:
        client = genai.Client(api_key=GOOGLE_API_KEY)
    except Exception as e:
        print(f"❌ 설정 에러: {e}")
        return

    # [승부수] 모델 이름을 'gemini-1.5-flash' (버전번호X) 로 강제 지정
    # 이 이름이 안되면 'gemini-1.5-flash-latest'를 씁니다.
    target_model = 'gemini-1.5-flash'
    print(f"🎯 타겟 모델: {target_model} (무료 티어 표준)")

    if not os.path.exists(image_folder): return
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png'))]
    if not image_files:
        print("❌ 사진이 없습니다.")
        return

    print(f"📸 {len(image_files)}장 분석 시작...")
    all_data = []

    for idx, img_file in enumerate(image_files):
        print(f"\n[{idx+1}/{len(image_files)}] {img_file}", end="")
        img_path = os.path.join(image_folder, img_file)
        
        try:
            image = Image.open(img_path)
            prompt = "Extract vehicle log to JSON: date, time, content, car_type, car_num, amount."

            # 모델 호출
            response = client.models.generate_content(
                model=target_model,
                contents=[prompt, image],
                config=types.GenerateContentConfig(response_mime_type='application/json')
            )

            if response.text:
                print(" -> 성공! ✅")
                json_data = json.loads(response.text)
                if isinstance(json_data, dict): json_data = [json_data]
                
                for item in json_data:
                    d = item.get('date', '')
                    c = item.get('content', '')
                    amt_raw = str(item.get('amount', 0))
                    a = int(re.sub(r'[^0-9]', '', amt_raw))
                    
                    all_data.append([d, item.get('time',''), c, item.get('car_type',''), item.get('car_num',''), a])
                    print(f"     결과: {d} | {a}원 | {c[:10]}")
            else:
                print(" -> 실패 (빈 응답)")

        except Exception as e:
            # 404가 뜨면 바로 별칭으로 바꿔서 재시도
            if "404" in str(e):
                print(f"\n     ⚠️ 1.5-flash 없음! 'latest' 버전으로 재시도합니다...")
                try:
                    response = client.models.generate_content(
                        model='gemini-1.5-flash-latest', # 별칭 사용
                        contents=[prompt, image],
                        config=types.GenerateContentConfig(response_mime_type='application/json')
                    )
                    if response.text:
                        print("     -> 재시도 성공! ✅")
                        # (데이터 처리 로직 동일)
                        json_data = json.loads(response.text)
                        if isinstance(json_data, dict): json_data = [json_data]
                        for item in json_data:
                            d = item.get('date', '')
                            a = int(re.sub(r'[^0-9]', '', str(item.get('amount', 0))))
                            all_data.append([d, item.get('time',''), item.get('content',''), item.get('car_type',''), item.get('car_num',''), a])
                            print(f"     결과: {d} | {a}원")
                except Exception as e2:
                    print(f"     ❌ 재시도도 실패: {e2}")
            elif "429" in str(e):
                print(f"\n     ⏳ 사용량 초과! 10초 대기...")
                time.sleep(10)
            else:
                print(f"\n     ⚠️ 에러: {e}")

        time.sleep(3)

    # 엑셀 저장
    if all_data:
        try:
            wb = openpyxl.load_workbook(template_path)
            ws = wb.active
            all_data.sort(key=lambda x: x[0])
            for i, row in enumerate(all_data):
                for c, val in enumerate(row):
                    try: ws.cell(row=START_ROW+i, column=c+1).value = val
                    except: pass
            wb.save(os.path.join(image_folder, "차량명세서_1.5.xlsx"))
            print("\n🎉 저장 완료!")
        except: pass

if __name__ == "__main__":
    run_alias_mode()