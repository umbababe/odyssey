import streamlit as st
import requests

# FastAPI 서버의 엔드포인트 URL
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
            if response.status_code == 200:
                st.success("Biometric data successfully sent!")
                st.write("Response from server:", response.json())
            else:
                st.error(f"Failed to send data. Server responded with status code {response.status_code}.")
        except Exception as e:
            st.error("An error occurred while sending data.")
            st.write(e)

# Text Input 탭
with tab2:
    st.header("Text Input")
    user_text = st.text_area("Type something here:")
    if st.button("Submit Text Input"):
        payload = {"type": "text_input", "user_text": user_text}
        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                st.success("Text data successfully sent!")
                st.write("Response from server:", response.json())
            else:
                st.error(f"Failed to send data. Server responded with status code {response.status_code}.")
        except Exception as e:
            st.error("An error occurred while sending data.")
            st.write(e)

# Emotion Selection 탭
with tab3:
    st.header("Emotion Selection")
    emotions = ["Happiness", "Sadness", "Anger", "Fear", "Disgust", "Love", "Guilt", "Surprise", "Shame", "Curiosity"]
    selected_emotions = st.multiselect("Select your emotions:", emotions)
    if st.button("Submit Emotion Selection"):
        payload = {"type": "emotion_selection", "selected_emotions": selected_emotions}
        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                st.success("Emotion data successfully sent!")
                st.write("Response from server:", response.json())
            else:
                st.error(f"Failed to send data. Server responded with status code {response.status_code}.")
        except Exception as e:
            st.error("An error occurred while sending data.")
            st.write(e)
