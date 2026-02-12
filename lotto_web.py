import streamlit as st
import random
import time

# 1. 페이지 설정
st.set_page_config(page_title="인생역전 로또", page_icon="🍀")

# --- [마법의 시작] 애니메이션 규칙을 미리 알려주기 ---
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
        font-size: 2.5rem; /* 크기를 조금 더 키웠어요! */
        animation: float 4s linear forwards; /* infinite 대신 1회 발사로 변경 */
        z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True
)

def clover_effect():
    # 클로버 15개를 생성!
    for i in range(15):
        left = random.randint(5, 95) # 화면 골고루 뿌리기
        delay = random.uniform(0, 2) # 나오는 시간차 두기
        st.markdown(f'<div class="clover" style="left: {left}vw; animation-delay: {delay}s;">🍀</div>', unsafe_allow_html=True)
# --- [마법의 끝] ---

# 2. 제목 꾸미기
st.title("💰 인생 역전! 로또 번호 생성기")
st.subheader("네잎클로버의 기운이 솟아납니다! 🍀")
st.write("버튼을 누르면 풍선, 눈, 그리고 클로버가 나타나요!")

if st.button("🍀 행운의 번호 뽑기! 🍀"):
    
    # 두근두근 효과
    with st.spinner('행운의 기운을 모으는 중...'):
        time.sleep(1)
    
    # 효과 3종 세트 동시 발사!
    st.balloons()    
    st.snow()        
    clover_effect()  

    st.success("🎉 당첨 기운 팍팍! 이번 주 주인공은 님입니다!")
    
    for i in range(1, 6):
        lotto_nums = random.sample(range(1, 46), 6)
        lotto_nums.sort()
        st.info(f"**{i}번째:** {lotto_nums}")

st.sidebar.markdown("---")
st.sidebar.write("🍀 클로버 효과 작동 중")