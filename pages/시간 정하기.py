import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="몇 시에 만날까?",
    page_icon="⏰",
    layout="centered"
)

# 2. 데이터 저장소 초기화 (오류 방지용)
if "votes" not in st.session_state:
    st.session_state.votes = {}  # {시간대: [이름1, 이름2...]} 구조로 변경

st.title("⏰ 몇 시에 만날까? 시간 조율기")
st.markdown("날짜 상관없이 **가장 많이 겹치는 만남 시간**을 자동으로 계산합니다.")
st.markdown("---")

# 3. 선택 가능한 시간대 정의
TIME_SLOTS = [
    "오전 (09:00 ~ 12:00)", 
    "점심/낮 (12:00 ~ 14:00)", 
    "오후 (14:00 ~ 18:00)", 
    "저녁/식사 (18:00 ~ 20:00)", 
    "야간/심야 (20:00 ~ 24:00)"
]

# 4. 입력 폼
st.header("👤 내 가능한 시간 입력")
with st.form(key="time_picker_form", clear_on_submit=True):
    name = st.text_input("이름 (닉네임)", placeholder="예: 홍길동")
    selected_slots = st.multiselect("가능한 시간대를 모두 골라주세요", TIME_SLOTS)
    submit = st.form_submit_button("등록하기")

# 5. 데이터 입력 처리 (예외 처리 포함)
if submit:
    clean_name = name.strip()
    if not clean_name:
        st.error("이름을 입력해야 등록할 수 있습니다.")
    elif not selected_slots:
        st.error("가능한 시간대를 최소 하나 이상 선택해 주세요.")
    else:
        # 시간대별로 이름 저장
        for slot in selected_slots:
            if slot not in st.session_state.votes:
                st.session_state.votes[slot] = []
            # 중복 투표 방지
            if clean_name not in st.session_state.votes[slot]:
                st.session_state.votes[slot].append(clean_name)
        st.success(f"🎉 {clean_name}님의 일정이 반영되었습니다!")

st.markdown("---")

# 6. 결과 출력 섹션
st.header("📊 실시간 투표 현황")

# 등록된 데이터가 있는지 확인
all_voters = set()
for voters in st.session_state.votes.values():
    all_voters.update(voters)

if not all_voters:
    st.info("아직 등록된 투표가 없습니다. 위 폼에서 시간대를 입력해 주세요!")
else:
    # 총 참여자 수
    total_users = len(all_voters)
    st.write(f"👥 **현재 참여 인원:** 총 {total_users}명 ({', '.join(all_voters)})")
    
    # 투표가 많은 순서대로 정렬하기 위해 리스트 변환
    results = []
    for slot in TIME_SLOTS:
        voters_list = st.session_state.votes.get(slot, [])
        results.append({
            "slot": slot,
            "count": len(voters_list),
            "voters": voters_list
        })
    
    # 득표수 기준 내림차순 정렬
    results.sort(key=lambda x: x["count"], reverse=True)
    
    # 결과 시각화
    st.subheader("💡 추천 만남 시간 순위")
    for res in results:
        if res["count"] > 0:
            # 참석율 계산
            percentage = int((res["count"] / total_users) * 100)
            voters_str = ", ".join(res["voters"])
            
            # 만장일치인 경우 초록색창, 아니면 일반 파란창
            if res["count"] == total_users:
                st.success(f"🔥 **[만장일치] {res['slot']}** ({res['count']}명 참여 / {percentage}%)  \n👉 참여자: {voters_str}")
            else:
                st.info(f"⭐ **{res['slot']}** ({res['count']}명 참여 / {percentage}%)  \n👉 참여자: {voters_str}")

    # 데이터 전체 초기화 버튼 (안전한 방식)
    st.markdown("---")
    if st.button("🔄 투표 데이터 전체 리셋"):
        st.session_state.votes = {}
        st.success("데이터가 초기화되었습니다. 새로고침(F5)을 하거나 다음 입력 시 반영됩니다.")
