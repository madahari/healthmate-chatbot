import streamlit as st
import requests

request_uri = ""
# Show title and description.
st.title("💬 Healthmate Chatbot")
st.write(
    "이것은 HealthMate 팀의 건강관련 질문에 답변을 하기위한 ChatBot 입니다."
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
    api_url = "https://3d61-223-171-90-226.ngrok-free.app/chat/"
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
    except RequestsJSONDecodeError:
        st.error("서버와 통신할 수 없습니다.")
