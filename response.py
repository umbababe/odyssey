# response.py

def handle_response(response):
    """
    FastAPI 응답 데이터를 처리하는 함수
    :param response: requests 라이브러리를 통해 받은 응답 객체
    :return: 처리된 메시지 또는 데이터
    """
    try:
        if response.status_code == 200:
            # JSON 응답 파싱
            data = response.json()
            return f"Success: {data.get('message', 'No message provided')}"
        else:
            return f"Error: Server returned status code {response.status_code}. Response: {response.text}"
    except Exception as e:
        return f"Error processing response: {e}"
