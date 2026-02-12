import tkinter as tk
import random

def generate_lotto():
    # 5번 반복해서 번호를 뽑아 저장할 리스트(바구니)
    result_list = []
    
    for i in range(1, 6): # 1부터 5까지 반복
        # 1. 번호 뽑기
        lotto_nums = random.sample(range(1, 46), 6)
        lotto_nums.sort()
        
        # 2. 예쁘게 글자 만들기 (예: "1게임 :  2  15  23 ...")
        # nums_str 변수에 번호들을 문자열로 변환해서 넣음
        nums_str = '  '.join(map(str, lotto_nums))
        game_str = f"{i}게임 :  {nums_str}"
        
        # 3. 리스트에 추가
        result_list.append(game_str)
    
    # 4. 화면에 보여주기 (줄바꿈 문자인 \n 으로 합치기)
    final_text = "\n\n".join(result_list)
    label_result.config(text=final_text)

# --- 윈도우 창 설정 ---
window = tk.Tk()
window.title("💰 인생 역전! 로또 5게임 💰")
window.geometry("400x500")  # 창 크기를 세로로 더 길게 늘렸어요 (300 -> 500)
window.resizable(False, False)

# 1. 제목
label_title = tk.Label(window, text="이번 주 대박 번호", font=("맑은 고딕", 20, "bold"))
label_title.pack(pady=20)

# 2. 결과 화면 (5줄이 나와야 하니 넉넉하게 잡음)
# text를 비워두면 처음엔 아무것도 안 보임
label_result = tk.Label(window, text="버튼을 눌러주세요!", font=("Arial", 18), justify="left") 
label_result.pack(pady=20)

# 3. 버튼
btn = tk.Button(window, text="5천 원어치 뽑기 (Click!)", font=("맑은 고딕", 15, "bold"), bg="gold", command=generate_lotto)
btn.pack(pady=20)

# 실행
window.mainloop()