```python
import streamlit as st

st.set_page_config(
    page_title="약속 장소 투표",
    page_icon="📍"
)

st.title("📍 약속 장소 투표")

places = ["두정동", "성성동", "신부동", "차암동"]

if "votes" not in st.session_state:
    st.session_state.votes = {place: 0 for place in places}

st.write("원하는 장소에 투표하세요!")

selected_place = st.radio(
    "장소 선택",
    places
)

if st.button("🗳️ 투표하기"):
    st.session_state.votes[selected_place] += 1
    st.success(f"{selected_place}에 투표되었습니다!")

st.divider()

st.subheader("현재 투표 현황")

for place in places:
    st.write(f"{place}: {st.session_state.votes[place]}표")

st.divider()

max_vote = max(st.session_state.votes.values())

if max_vote > 0:
    winners = [
        place
        for place, vote in st.session_state.votes.items()
        if vote == max_vote
    ]

    if len(winners) == 1:
        st.success(f"현재 1위: {winners[0]} ({max_vote}표)")
    else:
        st.info(
            f"공동 1위: {', '.join(winners)} ({max_vote}표)"
        )

if st.button("🔄 투표 초기화"):
    st.session_state.votes = {place: 0 for place in places}
    st.success("투표가 초기화되었습니다.")
```

```
```
