import streamlit as st
import random

st.set_page_config(page_title="click해 보살", page_icon="🎯")

st.title("🎯 click해 보살")
st.write("고민 또는 질문을 머릿속으로 생각하고, 버튼을 눌러주세요")

# 결정 리스트
question = st.text_input("당신의 고민을 입력하세요", placeholder="예: 오늘 치킨 먹을까?")

# 결정 버튼
if st.button("결정해줘!"):
    if question.strip() == "":
        st.warning("고민을 먼저 입력해주세요!")
    else:
        decisions = [
            "무조건 하세요! 🔥",
            "하지 마세요. 그냥 쉬는 게 좋아요. 😌",
            "한 번 해보고 결정해요! 🤔",
            "오늘은 넘어가고 내일 다시 고민해봐요. ⏳",
            "지금이 기회입니다. 잡으세요! 🏃‍♀️",
            "당장은 아니에요. 때를 기다려봐요. 🐢",
        ]
        choice = random.choice(decisions)
        st.success(f"💡 결정: **{choice}**")

        # 가벼운 이유 제공
        reasons = [
            "운명은 이미 정해져 있어요.",
            "당신의 뇌를 대신해서 저희가 계산해봤습니다.",
            "사실 저도 잘 모르지만 이게 느낌이 좋아요.",
            "고민할 시간에 행동하세요!",
            "오늘 운세가 좋아요. 믿어보세요!",
        ]
}
reasons = [
    "느낌이 왔어요. 바로 이거예요.",
    "운명의 신이 이렇게 말했습니다.",
    "제 주관 100%입니다. 그래도 믿어보세요!",
    "여기까지 온 것도 인연이에요.",
    "당신의 오늘 운세는 대박입니다!",
    "복잡할수록 단순하게!",
    "자신감을 가져요" 
]

fortunes = [
    "오늘은 좋은 일이 생길 거예요 🍀",
    "너무 조급해하지 말아요.",
    "말보다는 행동이 필요한 하루!",
    "당신은 이미 많은 걸 이뤘어요.",
    "마음 가는 대로 해도 괜찮아요.",
    "천천히 해보아요",
    "완전 럭키비키!",
    "*오늘의 주인공*"
]
# 버튼 클릭
 reason = random.choice(reasons)
        st.caption(f"🧠 이유: {reason}")
