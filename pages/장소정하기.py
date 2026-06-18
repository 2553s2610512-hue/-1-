```python
import streamlit as st
import random

st.set_page_config(
    page_title="약속 장소 정하기",
    page_icon="📍"
)

st.title("📍 약속 장소 랜덤 추천")
st.write("버튼을 눌러 오늘 만날 동네를 정해보세요!")

places = ["두정동", "신부동", "성성동", "차암동"]

if st.button("🎲 랜덤으로 동네 뽑기"):
    result = random.choice(places)

    st.balloons()

    st.success("약속 장소가 정해졌습니다!")

    st.markdown(
        f"""
        ## 📍 {result}
        """
    )

st.divider()

st.subheader("후보 동네")
for place in places:
    st.write(f"• {place}")
```
