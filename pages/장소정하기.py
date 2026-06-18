import streamlit as st
import random

st.set_page_config(
    page_title="약속 장소 정하기",
    page_icon="📍"
)

st.title("📍 약속 장소 랜덤 선택기")

places = ["두정동", "성성동", "신부동", "차암동"]

st.write("후보 장소")
for place in places:
    st.write("- " + place)

if st.button("🎲 랜덤으로 정하기"):
    result = random.choice(places)
    st.success(f"오늘의 약속 장소는 {result} 입니다!")
