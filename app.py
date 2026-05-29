# 간단한 Streamlit 싸움 대화 도움 앱

## 1. app.py

아래 내용만 그대로 복사해서 `app.py` 파일에 넣어.

```python
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
```

---

## 2. requirements.txt

아래 한 줄만 넣어.

```txt
streamlit
```

---

## 3. GitHub 업로드 방법

1. GitHub에서 새 저장소 만들기
2. `app.py` 와 `requirements.txt` 업로드
3. 커밋하기

---

## 4. Streamlit 배포 방법

1. Streamlit Cloud 접속
2. GitHub 연결
3. 저장소 선택
4. `app.py` 선택 후 Deploy 누르기

---

## 5. 실행 명령어

터미널에서:

```bash
streamlit run app.py
```

앱 실행 후 브라우저가 자동으로 열림.

