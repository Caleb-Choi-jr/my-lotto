import streamlit as st
import random
import time

# 1. 페이지 설정
st.set_page_config(page_title="인생역전 로또", page_icon="🍀")

# --- [마법의 시작] 네잎클로버가 떠다니는 효과 설정 ---
def clover_effect():
    st.markdown(
        """
        <style>
        @keyframes float {
            0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }
        .clover {
            position: fixed;
            bottom: -10vh;
            font-size: 2rem;
            animation: float 5s linear infinite;
            z-index: 9999;
        }
        </style>
        """, unsafe_allow_html=True
    )
    # 클로버 10개를 각기 다른 위치에서 발사!
    for i in range(10):
        left = random.randint(0, 90)
        delay = random.uniform(0, 5)
        st.markdown(f'<div class="clover" style="left: {left}vw; animation-delay: {delay}s;">🍀</div>', unsafe_allow_html=True)
# --- [마법의 끝] ---

# 2. 제목 꾸미기
st.title("💰 인생 역전! 로또 번호 생성기")
st.subheader("네잎클로버의 기운을 받아보세요! 🍀")

if st.button("🍀 행운의 번호 뽑기! 🍀"):
    
    # 뜸 들이기
    with st.spinner('행운의 네잎클로버를 찾고 있습니다...'):
        time.sleep(1.5)
    
    # 효과 3종 세트!
    st.balloons()    # 풍선 팡팡
    st.snow()        # 눈 내리기
    clover_effect()  # 네잎클로버 둥둥! (우리가 만든 마법)

    st.success("🎉 당첨 기운 팍팍! 번호가 나왔습니다!")
    
    for i in range(1, 6):
        lotto_nums = random.sample(range(1, 46), 6)
        lotto_nums.sort()
        st.info(f"**{i}번째 게임:** {lotto_nums}")

st.sidebar.info("네잎클로버 효과가 추가되었습니다! 🍀")