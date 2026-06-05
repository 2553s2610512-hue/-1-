import streamlit as st
import google.generativeai as genai

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💖",
    layout="centered"
)

st.title("💖 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# -----------------------------
# API 키 설정
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error(
        "GEMINI_API_KEY를 불러올 수 없습니다.\n"
        "Streamlit Secrets 설정을 확인하세요."
    )
    st.stop()

# -----------------------------
# 모델 생성
# -----------------------------
try:
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
except Exception as e:
    st.error(f"모델 생성 중 오류 발생: {e}")
    st.stop()

# -----------------------------
# 채팅 기록 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요 😊\n\n"
                "연애 고민, 썸, 짝사랑, 이별, 재회 등 "
                "무엇이든 편하게 이야기해 주세요!"
            )
        }
    ]

# -----------------------------
# 기존 채팅 표시
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.chat_input("고민을 입력하세요...")

if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # Gemini 형식으로 대화 이력 변환
        history = []

        for msg in st.session_state.messages[:-1]:
            if msg["role"] == "user":
                history.append(
                    {
                        "role": "user",
                        "parts": [msg["content"]]
                    }
                )
            elif msg["role"] == "assistant":
                history.append(
                    {
                        "role": "model",
                        "parts": [msg["content"]]
                    }
                )

        chat = model.start_chat(history=history)

        prompt = f"""
너는 따뜻하고 현실적인 연애상담 전문가다.

규칙:
- 공감하기
- 상황 분석하기
- 현실적인 조언 제시하기
- 공격적이거나 무례하지 않기
- 답변은 너무 길지 않게 작성

사용자:
{user_input}
"""

        response = chat.send_message(prompt)
        answer = response.text

    except Exception as e:
        answer = f"⚠️ 오류가 발생했습니다.\n\n{e}"

    # 답변 저장
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

# -----------------------------
# 대화 초기화
# -----------------------------
st.divider()

if st.button("🗑️ 대화 초기화"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요 😊\n\n"
                "연애 고민을 편하게 이야기해 주세요!"
            )
        }
    ]
    st.rerun()
