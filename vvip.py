import streamlit as st
import random

st.set_page_config(page_title="대신 결정해드립니다", page_icon="🎯")

# 🔊 효과음 삽입 (click.mp3 파일 필요)
st.markdown("""
<audio id="click-sound" src="click.mp3"></audio>
<script>
function playClickSound() {
    const audio = document.getElementById("click-sound");
    if (audio) {
        audio.currentTime = 0;
        audio.play();
    }
}
</script>
""", unsafe_allow_html=True)

st.title("🎯 대신 결정해드립니다")
st.write("고민을 입력하거나, 마음속에 떠올리고 버튼을 눌러보세요.")

# 🤔 고민 입력
user_question = st.text_input("고민이 있으신가요? (입력은 선택 사항)", placeholder="예: 이직할까요? 고백할까요?")

# 카테고리 선택
category = st.selectbox("고민의 카테고리를 선택하세요", ["전체", "연애", "일", "일상", "우정"])

# 카테고리별 결정 + 확률 조정
romance_answers = [
    "고백해보는 건 어때요? 💌",
    "기다려보세요. 때가 와요.",
    "지금은 혼자가 더 좋아요.",
    "그 사람도 당신 생각 중일지도 몰라요!",
    "마음을 전해보세요.",
    "고민할 필요 없어요, 그냥 해요! ✅",
    "하지 마세요. 후회할지도 몰라요. ❌",
    "바라는데로 되지 않을 수 있어요",
    "주변 사람에게 한번 물어보세요. 🗣️"
]
romance_weights = [0.1, 0.25, 0.1, 0.1, 0.25, 0.07, 0.07, 0.03, 0.03]

category_decisions = {
    "연애": (romance_answers, romance_weights),
    "일": [
        "이직을 고려해보세요.", "지금은 버틸 때!", "한 번 도전해보세요.",
        "휴가가 필요해 보여요.", "결과보다 과정이 중요해요.",
        "고민할 필요 없어요, 그냥 해요! ✅"
    ],
    "일상": [
        "산책을 해보는 건 어때요? 🚶‍♂️", "하루 푹 쉬어도 괜찮아요.",
        "새로운 취미를 찾아보세요.", "오늘은 내가 나를 위해!",
        "청소부터 해볼까요?", "내일로 미뤄보세요. ⏰"
    ],
    "우정": [
        "먼저 연락해보세요 ☎️", "가끔은 거리도 필요해요.",
        "그 친구도 당신을 생각하고 있어요.", "진심을 말해보세요.",
        "약속을 잡아보세요!", "하지 않는게 좋을 것 같아요.."
    ],
    "전체": [
        "지금 당장 해보세요! 🔥", "하지 마세요. 후회할지도 몰라요. ❌",
        "고민할 필요 없어요, 그냥 해요! ✅", "내일로 미뤄보세요. ⏰",
        "일단 밥 먹고 생각합시다. 🍚", "쉬는 것도 전략입니다. 😌",
        "주변 사람에게 한번 물어보세요. 🗣️", "마음이 더 끌리는 곳으로 가세요!",
        "하지 않는게 좋을 것 같아요..", "바라는데로 되지 않을 수 있어요"
    ]
}

reasons = [
    "느낌이 왔어요. 바로 이거예요.",
    "운명의 신이 이렇게 말했습니다.",
    "당신의 직감이 맞을 확률, 오늘 높습니다.",
    "여기까지 온 것도 인연이에요.",
    "고민이 깊을수록, 선택은 단순하게!",
    "자신감을 가져요!"
]

fortunes = [
    "오늘은 좋은 일이 생길 거예요 🍀",
    "너무 조급해하지 말아요.",
    "말보다는 행동이 필요한 하루!",
    "마음 가는 대로 해도 괜찮아요.",
    "천천히 해보아요.",
    "당신은 이미 잘하고 있어요. 👏"
]

# 🎲 버튼 클릭
if st.button("🔮 결정 내려줘!"):
    # 🔊 효과음 재생
    st.markdown("<script>playClickSound();</script>", unsafe_allow_html=True)

    # 결정
    if category == "연애":
        answers, weights = category_decisions["연애"]
        decision = random.choices(answers, weights=weights, k=1)[0]
    else:
        answers = category_decisions.get(category, category_decisions["전체"])
        decision = random.choice(answers)

    reason = random.choice(reasons)
    fortune = random.choice(fortunes)

    st.markdown("---")
    if user_question:
        st.markdown(f"**당신의 고민:** {user_question}")

    st.markdown(f"## ✅ 결정: {decision}")
    st.caption(f"🧠 이유: {reason}")
    st.markdown("---")
    st.caption("🌟 보살의 한 마디")
    st.write(fortune)
