import streamlit as st
import random

st.set_page_config(
page_title="약속 장소 정하기",
page_icon="📍",
layout="centered"
)

st.title("📍 약속 장소 랜덤 선택기")
st.write("오늘 만날 동네를 랜덤으로 정해보세요!")

st.divider()

st.subheader("후보 장소 선택")

dujeong = st.checkbox("두정동", value=True)
seongseong = st.checkbox("성성동", value=True)
sinbu = st.checkbox("신부동", value=True)
chaam = st.checkbox("차암동", value=True)

places = []

if dujeong:
places.append("두정동")

if seongseong:
places.append("성성동")

if sinbu:
places.append("신부동")

if chaam:
places.append("차암동")

st.divider()

if st.button("🎲 랜덤으로 장소 정하기", use_container_width=True):

```
if len(places) == 0:
    st.error("최소 한 개 이상의 장소를 선택해주세요.")
else:
    result = random.choice(places)

    st.balloons()

    st.success("약속 장소가 결정되었습니다!")

    st.markdown(
        f"""
        ## 📍 {result}
        """
    )
```

st.divider()

st.caption("두정동 · 성성동 · 신부동 · 차암동 중 랜덤 선택")
