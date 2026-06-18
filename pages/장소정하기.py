import streamlit as st
import random

st.set_page_config(
page_title="약속 장소 정하기",
page_icon="📍"
)

st.title("📍 약속 장소 랜덤 추천")

places = ["두정동", "신부동", "성성동", "차암동"]

if st.button("🎲 랜덤으로 동네 뽑기"):
result = random.choice(places)

```
st.balloons()
st.success(f"오늘의 약속 장소는 {result} 입니다!")
```

st.write("### 후보 동네")
for place in places:
st.write(f"• {place}")
