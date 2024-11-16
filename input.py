import streamlit as st
import requests

# Streamlit UI
st.header("Please tell me how you feel right now.")
current_feeling = st.text_area(
    "Describe your current feeling:",
    placeholder="Type how you feel right now..."
)

# FastAPI의 엔드포인트 URL
api_url = "https://abc.com/input"

# 버튼 클릭 시 API로 데이터 전송
if st.button("Submit"):
    if current_feeling:
        # 데이터 전송
        payload = {"feeling": current_feeling}  # FastAPI에 전송할 데이터
        try:
            response = requests.post(api_url, json=payload)
            
            # 응답 처리
            if response.status_code == 200:
                st.success("Your feeling has been successfully sent!")
                st.write("Response from server:", response.json())
            else:
                st.error(f"Failed to send data. Server responded with status code {response.status_code}.")
                st.write(response.text)
        except Exception as e:
            st.error("An error occurred while sending data.")
            st.write(e)
    else:
        st.warning("Please type your feeling before submitting.")
