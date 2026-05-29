# 간단한 Streamlit 싸움 대화 도움 앱

## 1. app.py

```python
import streamlit as st

st.title("싸움 대화 도우미")

situation = st.text_input("상황을 짧게 적어줘")

if st.button("답변 보기"):
    if situation:
        st.subheader("추천 말투")

        answers = [
            "내가 먼저 감정적으로 말한 건 미안해.",
            "네 입장도 이해하려고 노력할게.",
            "우리 차분하게 다시 이야기하자.",
            "상처 주려고 한 말은 아니었어.",
            "어떻게 하면 좋을지 같이 생각해보자."
        ]

        for answer in answers:
            st.write("- " + answer)
    else:
        st.warning("상황을 입력해줘!")
```

---

## 2. requirements.txt

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

