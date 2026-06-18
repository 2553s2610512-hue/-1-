import streamlit as st
from datetime import date, timedelta

st.set_page_config(
    page_title="약속 날짜 조율기",
    page_icon="📅",
    layout="wide"
)

st.title("📅 약속 날짜 조율기")
st.write("여러 사람이 가능한 날짜를 입력하여 공통 가능한 날짜를 찾아보세요.")

# 세션 상태 초기화
if "schedules" not in st.session_state:
    st.session_state.schedules = {}

# 날짜 범위 생성
today = date.today()
default_dates = [today + timedelta(days=i) for i in range(14)]

st.subheader("1️⃣ 참여자 일정 등록")

with st.form("schedule_form"):
    name = st.text_input("이름")

    selected_dates = st.multiselect(
        "가능한 날짜 선택",
        options=default_dates,
        format_func=lambda x: x.strftime("%Y-%m-%d")
    )

    submit = st.form_submit_button("일정 등록")

    if submit:
        try:
            if not name.strip():
                st.error("이름을 입력해주세요.")
            elif len(selected_dates) == 0:
                st.error("최소 1개 이상의 날짜를 선택해주세요.")
            else:
                st.session_state.schedules[name.strip()] = selected_dates
                st.success(f"{name}님의 일정이 저장되었습니다.")
        except Exception as e:
            st.error(f"오류 발생: {e}")

st.divider()

st.subheader("2️⃣ 등록된 참여자")

if st.session_state.schedules:
    for person, dates in st.session_state.schedules.items():
        date_text = ", ".join(
            d.strftime("%Y-%m-%d") for d in dates
        )
        st.write(f"**{person}** : {date_text}")
else:
    st.info("아직 등록된 일정이 없습니다.")

st.divider()

st.subheader("3️⃣ 공통 가능한 날짜 찾기")

if len(st.session_state.schedules) >= 2:

    all_date_sets = [
        set(dates)
        for dates in st.session_state.schedules.values()
    ]

    common_dates = set.intersection(*all_date_sets)

    if common_dates:
        st.success("🎉 모두 가능한 날짜")
        for d in sorted(common_dates):
            st.write(f"✅ {d.strftime('%Y-%m-%d')}")
    else:
        st.warning("모든 사람이 가능한 날짜가 없습니다.")

        st.write("### 📊 날짜별 가능 인원")

        count_dict = {}

        for dates in st.session_state.schedules.values():
            for d in dates:
                count_dict[d] = count_dict.get(d, 0) + 1

        sorted_dates = sorted(
            count_dict.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for d, cnt in sorted_dates:
            st.write(
                f"📅 {d.strftime('%Y-%m-%d')} → {cnt}명 가능"
            )

else:
    st.info("2명 이상 등록되면 공통 날짜를 계산합니다.")

st.divider()

st.subheader("4️⃣ 관리")

if st.button("전체 일정 초기화"):
    st.session_state.schedules = {}
    st.success("모든 일정이 삭제되었습니다.")
    st.rerun()
