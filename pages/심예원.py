import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 1. 페이지 설정
st.set_page_config(
    page_title="언제 만날까? - 약속 시간 조율기",
    page_icon="📅",
    layout="centered"
)

# 2. 세션 상태(Session State) 초기화 - 데이터 임시 저장용
if "participants" not in st.session_state:
    st.session_state.participants = []  # 참여자 명단 및 일정 저장

st.title("📅 언제 만날까? 약속 시간 조율기")
st.markdown("각자 가능한 날짜와 시간대를 입력하면, 가장 많이 겹치는 **최적의 만남 시간**을 찾아 드립니다!")
st.markdown("---")

# 3. 입력 섹션
st.header("👤 내 일정 입력하기")

with st.form(key="schedule_form", clear_on_submit=True):
    name = st.text_input("이름 (닉네임)", placeholder="예: 홍길동")
    
    # 오늘부터 2주 뒤까지 날짜 선택 가능하도록 설정
    today = datetime.today()
    available_date = st.date_input(
        "가능한 날짜 선택", 
        value=today,
        min_value=today,
        max_value=today + timedelta(days=14)
    )
    
    # 시간대 다중 선택 (오전, 오후, 저녁)
    available_times = st.multiselect(
        "가능한 시간대 (중복 선택 가능)",
        ["오전 (09:00 ~ 12:00)", "오후 (12:00 ~ 18:00)", "저녁 (18:00 ~ 22:00)"],
        default=["오후 (12:00 ~ 18:00)"]
    )
    
    submit_button = st.form_submit_button(label="일정 추가하기")

# 4. 데이터 추가 로직 및 예외 처리
if submit_button:
    if not name.strip():
        st.error("이름을 입력해 주세요!")
    elif not available_times:
        st.error("가능한 시간대를 최소 하나 이상 선택해 주세요!")
    else:
        # 데이터 저장
        date_str = available_date.strftime("%Y-%m-%d")
        for time_slot in available_times:
            st.session_state.participants.append({
                "이름": name.strip(),
                "날짜": date_str,
                "시간대": time_slot
            })
        st.success(f"🎉 {name}님의 일정이 성공적으로 추가되었습니다!")

st.markdown("---")

# 5. 현황 및 결과 분석 섹션
st.header("📊 우리의 일정 모아보기")

if not st.session_state.participants:
    st.info("아직 등록된 일정이 없습니다. 위 양식을 통해 일정을 먼저 등록해 주세요!")
else:
    # 데이터프레임 변환
    df = pd.DataFrame(st.session_state.participants)
    
    # 탭으로 화면 분할 (입력 현황 vs 최적의 시간 추천)
    tab1, tab2 = st.tabs(["👥 참여자별 현황", "🏆 최적의 만남 시간 추천"])
    
    with tab1:
        st.subheader("현재까지 참여한 멤버와 일정")
        st.dataframe(df, use_container_width=True)
        
        # 데이터 초기화 버튼
        if st.button("🔄 모든 데이터 초기화"):
            st.session_state.participants = []
            st.rerun()
            
    with tab2:
        st.subheader("💡 가장 많이 겹치는 시간대 순위")
        
        # 날짜와 시간대별로 그룹화하여 카운트 계산
        match_counts = df.groupby(["날짜", "시간대"]).agg(
            인원수=("이름", "count"),
            참여자=("이름", lambda x: ", ".join(list(set(x))))
        ).reset_index()
        
        # 인원수 기준 내림차순 정렬
        match_counts = match_counts.sort_values(by="인원수", ascending=False)
        
        # 고유 참여자 수 계산
        total_unique_users = len(df["이름"].unique())
        
        # 결과 출력
        for index, row in match_counts.iterrows():
            # 모두 참여 가능한 경우와 일부만 가능한 경우 색상 차별화
            if row['인원수'] == total_unique_users:
                badge = "🔥 [모두 가능]"
                st.success(f"{badge} **{row['날짜']} ({row['시간대']})** - 참여 인원: {row['인원수']}명 ({row['참여자']})")
            else:
                badge = "⭐ [추천]"
                st.info(f"{badge} **{row['날짜']} ({row['시간대']})** - 참여 인원: {row['인원수']}명 ({row['참여자']})")
