import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="모여라 시간표", page_icon="⏰", layout="wide")

st.title("⏰ 모여라 시간표 : 약속 시간 조율기")
st.caption("서로 가능한 시간을 입력하면, 가장 만나기 좋은 최적의 시간을 찾아드립니다!")

# 2. 세션 상태(데이터 저장소) 초기화
if "time_data" not in st.session_state:
    # 샘플 데이터 미리 넣어두기 (앱이 처음부터 예쁘게 보이도록)
    st.session_state.time_data = {
        "홍길동": ["12:00 - 14:00", "14:00 - 16:00", "18:00 - 20:00"],
        "김철수": ["12:00 - 14:00", "16:00 - 18:00", "18:00 - 20:00"],
        "이영희": ["12:00 - 14:00", "14:00 - 16:00", "16:00 - 18:00"]
    }

# 3. 레이아웃 분할 (왼쪽: 시간 입력 / 오른쪽: 결과 대시보드)
col1, col2 = st.columns([1, 2])

# 선택 가능한 시간대 정의
TIME_SLOTS = [
    "10:00 - 12:00",
    "12:00 - 14:00 (점심)",
    "14:00 - 16:00",
    "16:00 - 18:00",
    "18:00 - 20:00 (저녁)",
    "20:00 - 22:00"
]

# --- 왼쪽 사이드: 시간 입력 폼 ---
with col1:
    st.header("✍️ 내 가능 시간 넣기")
    with st.form(key="time_form", clear_on_submit=True):
        name = st.text_input("이름을 입력하세요:", placeholder="예: 홍길동")
        available_slots = st.multiselect(
            "만날 수 있는 시간을 모두 골라주세요 (중복 선택 가능):",
            options=TIME_SLOTS
        )
        submit_btn = st.form_submit_button(label="제출하기")
        
        if submit_btn:
            if not name.strip():
                st.error("이름을 입력해 주세요!")
            elif not available_slots:
                st.error("시간을 최소 하나 이상 선택해 주세요!")
            else:
                # 정규화를 위해 (점심), (저녁) 텍스트 제거 후 저장
                clean_slots = [slot.split(" (")[0] for slot in available_slots]
                st.session_state.time_data[name.strip()] = clean_slots
                st.success(f"✨ {name}님의 시간이 반영되었습니다!")

    # 데이터 초기화 버튼
    if st.button("🔄 전체 기록 초기화"):
        st.session_state.time_data = {}
        st.rerun()

# 전처리용 기준 시간대 (텍스트 깔끔하게 정리)
CLEAN_TIME_SLOTS = [t.split(" (")[0] for t in TIME_SLOTS]

# --- 오른쪽 사이드: 결과 시각화 및 AI 추천 ---
with col2:
    st.header("📊 현재 조율 현황")
    
    if not st.session_state.time_data:
        st.info("아직 입력된 시간이 없습니다. 왼쪽에서 대화를 시작해 보세요!")
    else:
        # 데이터프레임 생성을 위한 정렬
        summary_dict = {slot: 0 for slot in CLEAN_TIME_SLOTS}
        attendees_by_time = {slot: [] for slot in CLEAN_TIME_SLOTS}
        
        for person, slots in st.session_state.time_data.items():
            for slot in slots:
                if slot
