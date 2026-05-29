import streamlit as st

st.title("싸움 대화 도우미")

situation = st.text_input("상황을 짧게 적어줘")

if st.button("답변 보기"):
    if situation:
        st.subheader("추천 말투")

        answers = [
            "그렇게 말하면 기분 나쁘니까 말투 좀 조심해.",
            "나도 계속 참기만 하는 건 힘들어.",
            "억울한 건 알겠는데 사람 무시하듯 말하진 마.",
            "싸우자는 거면 나도 할 말 많아.",
            "서로 감정 상하기 전에 적당히 하자."
        ]

        for answer in answers:
            st.write("- " + answer)
    else:
        st.warning("상황을 입력해줘!")
