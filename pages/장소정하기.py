import streamlit as st

st.set_page_config(
    page_title="약속 장소 투표",
    page_icon="📍"
)

st.title("📍 약속 장소 정하기")

if "places" not in st.session_state:
    st.session_state.places = []

if "votes" not in st.session_state:
    st.session_state.votes = {}

new_place = st.text_input("장소 입력")

if st.button("장소 추가"):
    place = new_place.strip()

    if place:
        if place not in st.session_state.places:
            st.session_state.places.append(place)
            st.session_state.votes[place] = 0

if st.session_state.places:

    selected = st.radio(
        "투표할 장소 선택",
        st.session_state.places
    )

    if st.button("투표하기"):
        st.session_state.votes[selected] += 1

    st.write("### 투표 현황")

    for place in st.session_state.places:
        st.write(
            f"{place}: {st.session_state.votes[place]}표"
        )
else:
    st.info("먼저 장소를 추가하세요.")
