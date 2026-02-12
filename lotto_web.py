import streamlit as st
import random
import time

# 1. 페이지 설정 (브라우저 탭에 표시될 이름과 아이콘)
st.set_page_config(page_title="인생역전 로또", page_icon="💰")

# 2. 제목 꾸미기
st.title("💰 인생 역전! 로또 번호 생성기")
st.markdown("---") # 구분선 추가
st.subheader("이번 주 행운의 주인공은 바로 당신입니다! 😎")

# 3. 버튼 만들기
if st.button("🍀 행운의 5천 원어치 뽑기 (클릭!) 🍀"):
    
    # 두근두근 긴장감 조성 (스피너)
    with st.spinner('행운의 기운을 모으고 있습니다... 잠시만 기다려주세요!'):
        time.sleep(2) # 2초 동안 뜸 들이기
    
    # --- 시각 효과 팡팡! ---
    st.balloons() # 풍선 효과
    st.snow()     # 눈 내리는 효과
    # ----------------------

    st.success("🎉 축하합니다! 분석이 완료되었습니다. 이번 주 1등 당첨 가즈아~!")
    
    # 4. 5게임 생성 및 출력
    for i in range(1, 6):
        # 1~45 사이의 숫자 중 6개 중복 없이 추출
        lotto_nums = random.sample(range(1, 46), 6)
        lotto_nums.sort() # 번호 순서대로 정렬
        
        # 보기 좋게 꾸며서 출력
        st.write(f"### **{i}번째 게임**")
        
        # 번호들을 예쁜 파란색 박스 안에 출력
        num_str = '  |  '.join(map(str, lotto_nums))
        st.info(f"✨ {num_str} ✨")
        
    st.markdown("---")
    st.warning("⚠️ 재미로만 즐겨주세요! 당첨되면 잊지 마시고 연락주세요. 😉")

# 5. 사이드바 (옆쪽 메뉴)
with st.sidebar:
    st.title("🛠️ 옵션 메뉴")
    st.write("로또 당첨 확률은 $1/8,145,060$ 입니다.")
    st.write("하지만 님은 할 수 있습니다!")
    if st.button("새로고침"):
        st.rerun()