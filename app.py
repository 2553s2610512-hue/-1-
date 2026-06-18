import streamlit as st

st.set_page_config(
page_title="MeetPoint",
page_icon="📍",
layout="wide"
)

st.markdown("""

<style>

.stApp{
    background: linear-gradient(180deg,#f7fbff 0%,#eef5ff 100%);
}

.hero{
    text-align:center;
    padding-top:90px;
    padding-bottom:90px;
}

.title{
    font-size:72px;
    font-weight:800;
    color:#0A4DFF;
    margin-bottom:10px;
}

.subtitle{
    font-size:24px;
    color:#4a5568;
    margin-bottom:40px;
}

.feature-box{
    background:white;
    border-radius:20px;
    padding:25px;
    text-align:center;
    box-shadow:0 8px 25px rgba(0,0,0,0.08);
    border:1px solid #e6eefc;
}

.feature-title{
    font-size:22px;
    font-weight:700;
    color:#0A4DFF;
}

.feature-desc{
    color:#666;
    margin-top:8px;
}

.footer{
    text-align:center;
    color:#7a7a7a;
    margin-top:60px;
}
</style>

""", unsafe_allow_html=True)

st.markdown("""

<div class="hero">
    <div class="title">📍 MeetPoint</div>
    <div class="subtitle">
        약속을 더 쉽게 ✨
        <br><br>
        날짜, 시간, 장소를 함께 정하고
        모두가 편한 일정을 만들어보세요.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
st.markdown(""" <div class="feature-box"> <div class="feature-title">📅</div> <div class="feature-desc">날짜 조율</div> </div>
""", unsafe_allow_html=True)

with col2:
st.markdown(""" <div class="feature-box"> <div class="feature-title">⏰</div> <div class="feature-desc">시간 선택</div> </div>
""", unsafe_allow_html=True)

with col3:
st.markdown(""" <div class="feature-box"> <div class="feature-title">📍</div> <div class="feature-desc">장소 결정</div> </div>
""", unsafe_allow_html=True)

with col4:
st.markdown(""" <div class="feature-box"> <div class="feature-title">🤝</div> <div class="feature-desc">일정 공유</div> </div>
""", unsafe_allow_html=True)

st.markdown("""

<div class="footer">
    Blue & White Premium Theme 💙
</div>
""", unsafe_allow_html=True)
"""
