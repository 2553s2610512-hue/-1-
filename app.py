import streamlit as st
from datetime import date

# 페이지 설정
st.set_page_config(
    page_title="BlueMeet",
    page_icon="📅",
    layout="centered"
)

# 스타일
st.markdown("""
<style>
.main {
    background-color: #f5f9ff;
}

.hero {
    background: linear-gradient(135deg, #0A4DFF, #4F8DFF);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}

.hero-title {
    font-size: 40px;
    font-weight: 800;
}

.hero-sub {
    font-size: 18px;
    opacity: 0.95;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #0A4DFF;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.label {
    color: #0A4DFF;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 상단 Hero
st.markdown("""
<div class="hero">
    <div class="hero-title">BlueMeet</div>
    <div class="hero-sub">
        약속 날짜, 시간, 장소를 빠르게 정리하는 심플한 일정 조율 도구
    </div>
</div>
""", unsafe_allow_html=True)

st.write("### 📌 약속 정보 입력")

# 예외 처리용 기본값
try:
    title = st.text_input(
        "약속 제목",
        placeholder="예: 팀 미팅"
    )

    meeting_date = st.date_input(
        "날짜 선택",
        value=date.today()
    )

    meeting_time = st.time_input(
        "시간 선택"
    )

    location = st.text_input(
        "장소",
        placeholder="예: 강남역 스타벅스"
    )

    memo = st.text_area(
        "메모",
        placeholder="참석 인원, 준비물 등을 적어보세요."
    )

    st.divider()

    if st.button("약속 정리하기", use_container_width=True):

        if not title.strip():
            st.warning("약속 제목을 입력해주세요.")
        else:
            st.markdown(f"""
            <div class="card">
                <h3>📅 약속 요약</h3>
                <p><span class="label">제목</span><br>{title}</p>
                <p><span class="label">날짜</span><br>{meeting_date}</p>
                <p><span class="label">시간</span><br>{meeting_time.strftime('%H:%M')}</p>
                <p><span class="label">장소</span><br>{location if location else "미정"}</p>
                <p><span class="label">메모</span><br>{memo if memo else "없음"}</p>
            </div>
            """, unsafe_allow_html=True)

            st.success("약속 정보가 정리되었습니다.")

except Exception as e:
    st.error("오류가 발생했습니다.")
    st.exception(e)

# 하단 설명
st.markdown("---")
st.caption(
    "BlueMeet는 약속 날짜, 시간, 장소를 간단하게 정리하기 위한 Streamlit 웹앱입니다."
)
