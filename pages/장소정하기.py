import streamlit as st
import random

st.set_page_config(
    page_title="약속 장소 랜덤 정하기",
    page_icon="📍",
    layout="centered"
)

st.title("📍 약속 장소 랜덤 정하기")
st.write("각자 가능한 장소를 입력한 뒤 랜덤으로 장소를 정해보세요!")

# 세션 상태 초기화
if "people" not in st.session_state:
    st.session_state.people = []

st.divider()

st.subheader("👤 참가자 추가")

with st.form("add_person"):
    name = st.text_input("이름")

    places_text = st.text_area(
        "가능한 장소 입력 (한 줄에 하나씩)",
        placeholder="천안역\n신세계백화점\n터미널"
    )

    submitted = st.form_submit_button("추가하기")

    if submitted:
        name = name.strip()

        places = [
            place.strip()
            for place in places_text.split("\n")
            if place.strip()
        ]

        if not name:
            st.error("이름을 입력해주세요.")
        elif not places:
            st.error("최소 1개 이상의 장소를 입력해주세요.")
        else:
            st.session_state.people.append(
                {
                    "name": name,
                    "places": places
                }
            )
            st.success(f"{name}님이 추가되었습니다!")

st.divider()

st.subheader("📋 현재 참가자")

if st.session_state.people:
    for idx, person in enumerate(st.session_state.people, start=1):
        st.write(
            f"**{idx}. {person['name']}** → {', '.join(person['places'])}"
        )
else:
    st.info("아직 참가자가 없습니다.")

st.divider()

st.subheader("🎲 장소 랜덤 선택")

all_places = []

for person in st.session_state.people:
    all_places.extend(person["places"])

# 중복 제거
unique_places = list(dict.fromkeys(all_places))

st.write(f"현재 후보 장소 수: **{len(unique_places)}개**")

if unique_places:
    with st.expander("후보 장소 보기"):
        for place in unique_places:
            st.write(f"• {place}")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 랜덤 장소 뽑기", use_container_width=True):
        if not unique_places:
            st.warning("장소 후보가 없습니다.")
        else:
            result = random.choice(unique_places)

            st.balloons()

            st.success("약속 장소가 결정되었습니다!")
            st.markdown(
                f"""
                ## 📍 {result}
                """
            )

with col2:
    if st.button("🗑️ 전체 초기화", use_container_width=True):
        st.session_state.people = []
        st.rerun()

st.divider()

st.caption(
    "Tip: 각자 가능한 장소를 입력하면 모든 후보를 모아 랜덤으로 선정합니다."
) 
