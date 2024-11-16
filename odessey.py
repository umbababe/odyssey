import streamlit as st

# 첫 번째 선택 박스
st.header("Please tell me how you feel right now.")
current_feeling = st.text_area(
    "Describe your current feeling:",
    placeholder="Type how you feel right now..."
)

# 출력
st.write(f"You are feeling: {current_feeling}")

# 감정 선택 섹션
st.header("Please choose your feelings. (Select at least 3 - mixed emotions)")

# 감정 카테고리와 옵션
emotions = {
    "Joy": ["Happiness", "Satisfaction", "Delight", "Euphoria", "Gratitude"],
    "Anger": ["Annoyance", "Irritation", "Rage", "Discontent", "Frustration"],
    "Sadness": ["Depression", "Loneliness", "Grief", "Regret", "Sorrow"],
    "Fear": ["Terror", "Anxiety", "Worry", "Panic", "Dread"],
    "Disgust": ["Discomfort", "Contempt", "Aversion", "Loathing", "Revulsion"],
    "Love": ["Affection", "Passion", "Devotion", "Intimacy", "Compassion"],
    "Guilt": ["Regret", "Remorse", "Repentance", "Atonement", "Conscience"],
    "Surprise": ["Amazement", "Shock", "Wonder", "Unexpectedness", "Astonishment"],
    "Shame": ["Embarrassment", "Self-Consciousness", "Humiliation", "Mortification", "Shyness"],
    "Curiosity": ["Inquisitiveness", "Interest", "Eagerness to Learn", "Investigativeness", "Fascination"],
}

# 감정별 선택 박스 생성
selected_emotions = []
for category, feelings in emotions.items():
    selected = st.multiselect(f"- {category} -", feelings)
    selected_emotions.extend(selected)

# 최소 3개 감정 선택 체크
if len(selected_emotions) < 3:
    st.warning("Please select at least 3 emotions.")
else:
    st.success(f"You have selected {len(selected_emotions)} emotions.")
    st.write("Selected emotions:", selected_emotions)


