import streamlit as st
import random

st.set_page_config(page_title="대신 결정해드립니다", page_icon="🎯")

st.title("🎯 대신 결정해드립니다")
st.write("고민 또는 질문을 머릿속으로 생각하고, 버튼을 눌러주세요")

# 결정 리스트
decisions = [
    "지금 당장 해보세요! 🔥",
    "하지 마세요. 후회할지도 몰라요. ❌",
    "고민할 필요 없어요, 그냥 해요! ✅",
    "내일로 미뤄보세요. ⏰",
    "일단 밥 먹고 생각합시다. 🍚",
    "쉬는 것도 전략입니다. 😌",
    "주변 사람에게 한번 물어보세요. 🗣️",
    "뽑기 돌려보는 건 어때요? 🎡",
]

reasons = [
    "느낌이 왔어요. 바로 이거예요.",
    "운명의 신이 이렇게 말했습니다.",
    "제 주관 100%입니다. 그래도 믿어보세요!",
    "여기까지 온 것도 인연이에요.",
    "당신의 오늘 운세는 대박입니다!",
    "복잡할수록 단순하게!",
]

# 버튼
if st.button("🎲 결정해줘!"):
    decision = random.choice(decisions)
    reason = random.choice(reasons)

    st.markdown(f"## ✅ {decision}")
    st.caption(f"🧠 이유: {reason}")
