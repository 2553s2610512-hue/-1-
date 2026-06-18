import streamlit as st

st.set_page_config(
    page_title="약속 장소 투표",
    page_icon="📍"
)

st.title("📍 약속 장소 정하기")

if "places" not in st.session_state:
    st.session_state["places"] = []

if "votes" not in st.session_state:
    st.session_state["votes"] = {}

st.subheader("➕ 장소 추가")

new_place = st.text_input("가능한 장소를 입력하세요")

col1, col2 = st.columns(2)

with col1:
    if st.button("장소 추가"):
        place = new_place.strip()

        if place == "":
            st.warning("장소를 입력해주세요.")
        elif place in st.session_state["places"]:
            st.warning("이미 추가된 장소입니다.")
        else:
            st.session_state["places"].append(place)
            st.session_state["votes"][place] = 0
            st.success(f"{place} 추가 완료!")

with col2:
    if st.button("🔄 전체 초기화"):
        st.session_state["places"] = []
        st.session_state["votes"] = {}
        st.success("초기화 완료!")

st.divider()

if len(st.session_state["places"]) > 0:

    selected_place = st.radio(
        "투표할 장소를 선택하세요",
        st.session_state["places"]
    )

    if st.button("🗳️ 투표하기"):
        st.session_state["votes"][selected_place] += 1
        st.success(f"{selected_place}에 투표했습니다!")

    st.divider()

    st.subheader("📊 투표 현황")

    for place in st.session_state["places"]:
        st.write(
            f"📍 {place}: {st.session_state['votes'][place]}표"
        )

    max_vote = max(st.session_state["votes"].values())

    if max_vote > 0:
        winners = []

        for place, vote in st.session_state["votes"].items():
            if vote == max_vote:
                winners.append(place)

        st.divider()

        if len(winners) == 1:
            st.success(
                f"🏆 현재 1위: {winners[0]} ({max_vote}표)"
            )
        else:
            st.info(
                f"🤝 공동 1위: {', '.join(winners)} ({max_vote}표)"
            )

else:
    st.info("먼저 장소를 추가해주세요.")
