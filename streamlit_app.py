import streamlit as st
import requests

request_uri = ""
# Show title and description.
st.title("💬 Healthmate Chatbot")
# 디자인적용
    # Page config
    st.set_page_config(
        page_title="Health Mate",
        page_icon="🏥",
        layout="wide"
    )

    # CSS for custom styling
    st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .section-text {
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Onboarding Section 1
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="main-title">언제 어디서나,<br>내 손 안의 건강 비서<br>Health Mate</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Health Mate에 오신 것을 환영합니다!<br>건강 관리의 새로운 동반자를 만나보세요.</div>', 
                   unsafe_allow_html=True)
        
        # Here you would load and display the online-learning0.svg image
        st.image("online-learning0.svg", use_column_width=True)

    st.divider()

    # Onboarding Section 2
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Here you would load and display the group0.svg image
        st.image("group0.svg", use_column_width=True)
        
        st.markdown('<div class="section-title">궁금한 증상이나 질병에<br>대해 질문해주세요.</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="section-text">궁금한 증상이나 질병이 있다면 언제든지 질문해 주세요. '
                   '전문가 수준의 정보를 친절하게 안내해 드릴게요.</div>', 
                   unsafe_allow_html=True)

    st.divider()

    # Onboarding Section 3
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Here you would load and display the subscribe0.svg image
        st.image("subscribe0.svg", use_column_width=True)
        
        st.markdown('<div class="section-title">맞춤형 정보 제공으로<br>쉽고, 자세하게 알려드려요.</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="section-text">여러분에게 가장 관련성 높은 정보를 쉽고 자세하게<br>'
                   '제공해 드릴게요.</div>', 
                   unsafe_allow_html=True)
# 디자인적용 끝        

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
    api_url = "https://36a5-124-58-113-155.ngrok-free.app/chat/"
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
