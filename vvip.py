import streamlit as st
import random

st.set_page_config(page_title="대신 결정해드립니다", page_icon="🎲")

st.title("🎲 대신 결정해드립니다")
st.write("고민은 많고 결정은 어려울 때, 우리가 대신 결정해드릴게요.!!")

# 사용자 입력
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
        reason = random.choice(reasons)
        st.caption(f"🧠 이유: {reason}")
