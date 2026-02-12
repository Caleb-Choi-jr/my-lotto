import streamlit as st
import random
import time

# 1. 페이지 설정
st.set_page_config(page_title="황금빛 로또 당첨", page_icon="💰")

# --- [마법의 디자인 코드] 금색 배경 & 클로버 애니메이션 ---
st.markdown(
    """
    <style>
    /* 전체 배경을 금색 그라데이션으로 변경 */
    .stApp {
        background: linear-gradient(135deg, #ffd700, #ffecb3, #fbc02d);
        color: #3e2723; /* 글자색은 진한 갈색으로 */
    }
    
    /* 네잎클로버 애니메이션 정의 */
    @keyframes floatUp {
        0% { transform: translateY(110vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-20vh) rotate(720deg); opacity: 0; }
    }
    
    .clover {
        position: fixed;
        z-index: 999999; /* 모든 것보다 위에 표시 */
        font-size: 3rem;
        pointer-events: none; /* 클릭 방해 금지 */
        animation: floatUp 5s linear forwards;
    }
    
    /* 버튼 디자인도 금색에 어울리게 */
    .stButton>button {
        background-color: #ff6f00 !important;
        color: white !important;
        border-radius: 20px;
        border: 2px solid #ffccbc;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)

def show_clovers():
    # 클로버 20개를 화면 곳곳에 생성
    for _ in range(20):
        left = random.randint(0, 95)
        delay = random.uniform(0, 3)
        st.markdown(
            f'<div class="clover" style="left: {left}vw; animation-delay: {delay}s;">🍀</div>', 
            unsafe_allow_html=True
        )

# 2. 메인 화면 구성
st.title("💰 황금빛 기운! 로또 당첨 생성기")
st.header("이번 주 1등은 무조건 당신입니다! 😎")

if st.button("✨ 황금 번호 추출하기 (클릭) ✨"):
    
    # 두근두근 효과
    with st.spinner('황금 기운을 모으고 있습니다...'):
        time.sleep(1)
    
    # 시각 효과 3종 세트 발사!
    st.balloons()    # 풍선
    st.snow()        # 눈
    show_clovers()   # 네잎클로버 (강제 소환)

    st.success("🎉 축하합니다! 황금빛 당첨 번호입니다!")
    
    # 5게임 생성
    for i in range(1, 6):
        nums = sorted(random.sample(range(1, 46), 6))
        st.subheader(f"第 {i} 게임: {', '.join(map(str, nums))}")
        
    st.balloons() # 마지막에 한 번 더 축하!

st.sidebar.warning("⚠️ 이 사이트를 열어두면 금전운이 상승합니다(믿거나 말거나!)")