import streamlit as st

st.set_page_config(
    page_title="BlueMeet",
    page_icon="📅",
    layout="wide"
)

st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg, #0A4DFF, #4F8DFF);
    padding: 60px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.hero-title {
    font-size: 60px;
    font-weight: 800;
}

.hero-sub {
    font-size: 22px;
    margin-top: 15px;
}

.feature {
    background: white;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 15px;
    border-left: 5px solid #0A4DFF;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

.quote {
    text-align: center;
    font-size: 22px;
    color: #0A4DFF;
    margin-top: 50px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">📅 BlueMeet</div>
    <div class="hero-sub">
        약속을 더 쉽고 빠르게 ✨
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 서비스 소개

BlueMeet는 약속 날짜, 시간, 장소를 함께 정하고
참여자 모두가 편한 일정을 만들 수 있도록 도와주는 서비스입니다.
""")

st.markdown("""
<div class="feature">
<h4>📅 날짜 조율</h4>
후보 날짜를 비교하고 가장 적합한 일정을 선택할 수 있습니다.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature">
<h4>⏰ 시간 조율</h4>
참여 가능한 시간을 확인하고 효율적으로 약속을 정할 수 있습니다.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature">
<h4>📍 장소 결정</h4>
모두에게 편리한 장소를 선택할 수 있습니다.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature">
<h4>🤝 일정 공유</h4>
확정된 약속 정보를 간편하게 공유할 수 있습니다.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote">
"좋은 약속은 좋은 일정 조율에서 시작됩니다."
</div>
""", unsafe_allow_html=True)
