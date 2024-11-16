import streamlit as st
import requests
from response import handle_response  # response.py의 handle_response 함수 임포트

# FastAPI 서버 URL
api_url = "http://localhost:8000/input"

# 탭 생성
tabs = ["Biometric", "Text Input", "Emotion Selection"]
tab1, tab2, tab3 = st.tabs(tabs)

# Biometric 탭
with tab1:
    st.header("Biometric Information")
    birth_date = st.date_input("Enter your birth date:")
    if st.button("Submit Biometric"):
        payload = {"type": "biometric", "birth_date": str(birth_date)}
        try:
            response = requests.post(api_url, json=payload)
            message = handle_response(response)  # 응답 처리 함수 호출
            st.write(message)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Text Input 탭
with tab2:
    st.header("Text Input")
    user_text = st.text_area("Type something here:")
    if st.button("Submit Text Input"):
        payload = {"type": "text_input", "user_text": user_text}
        try:
            response = requests.post(api_url, json=payload)
            message = handle_response(response)  # 응답 처리 함수 호출
            st.write(message)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Emotion Selection 탭
with tab3:
    st.header("Emotion Selection")
    emotions = ["Happiness", "Sadness", "Anger", "Fear", "Disgust", "Love", "Guilt", "Surprise", "Shame", "Curiosity"]
    selected_emotions = st.multiselect("Select your emotions:", emotions)
    if st.button("Submit Emotion Selection"):
        payload = {"type": "emotion_selection", "selected_emotions": selected_emotions}
        try:
            response = requests.post(api_url, json=payload)
            message = handle_response(response)  # 응답 처리 함수 호출
            st.write(message)
        except Exception as e:
            st.error(f"An error occurred: {e}")
