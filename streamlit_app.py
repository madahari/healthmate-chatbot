import streamlit as st
import requests

request_uri = ""
# Show title and description.
st.title("💬 Healthmate Chatbot")
st.write(
    "안녕하세요, 질병은 우리 모두를 힘들게 합니다.\n\n"
    "이 봇의 목적은 기본적인 의료 정보와 조언을 제공함과 동시에 실제 의료 전문가의 진단을 받아 고통을 줄이고 더 큰 질병을 예방하는 것을 목표로 합니다.\n\n"
    "궁금한 증상이 무엇인가요? 어떤 의료 조언을 받고 싶으신가요?"
)

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("질문을 입력하세요."):
    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    api_url = "https://0bc4-124-58-113-155.ngrok-free.app/chat/"
    request_uri = api_url + prompt

# Stream the response to the chat using `st.write_stream`, then store it in 
# session state.
with st.chat_message("assistant"):
    try:
        if request_uri:
            data = requests.get(request_uri).json()
            if data:
                response = data['message'].replace("~", "\~")
                display_text = response.split("참고문헌:")
                st.markdown(display_text[0])
                if len(display_text) > 1:
                    st.info('**참고문헌:**' + display_text[1])
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.write("답변을 얻지 못했습니다.")
    except Exception:
        st.error("서버와 통신할 수 없습니다.")
