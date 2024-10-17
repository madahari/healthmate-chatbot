import streamlit as st
import requests

# Page config should be at the top
st.set_page_config(
    page_title="Health Mate",
    page_icon="🏥",
    layout="wide"
)

# CSS to create two distinct sections
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Create fixed top section */
    .fixed-content {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: white;
        z-index: 999;
        padding: 2rem;
        height: 100vh;
        overflow-y: auto;
    }
    
    /* Create scrollable chat section */
    .chat-section {
        position: absolute;
        top: 100vh;
        left: 0;
        right: 0;
        background: white;
        min-height: 100vh;
        padding: 2rem;
    }
    
    /* Styling */
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
    
    /* Chat container styling */
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Make chat input sticky at bottom */
    .stChatInputContainer {
        position: sticky;
        bottom: 0;
        background: white;
        padding: 1rem 0;
        z-index: 1000;
    }
</style>

<script>
    // Disable automatic scrolling
    window.addEventListener('DOMContentLoaded', (event) => {
        const preventScroll = () => {
            const urlParams = new URLSearchParams(window.location.search);
            if (!urlParams.has('chat')) {
                window.scrollTo(0, 0);
            }
        };
        
        window.addEventListener('scroll', preventScroll);
        
        // Add click handler to "Start Chat" button
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('start-chat')) {
                window.removeEventListener('scroll', preventScroll);
                const chatSection = document.querySelector('.chat-section');
                chatSection.scrollIntoView({ behavior: 'smooth' });
                window.history.pushState({}, '', '?chat=true');
            }
        });
    });
</script>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
    
# Fixed top section
st.markdown('<div class="fixed-content">', unsafe_allow_html=True)

def render_onboarding():
    # Onboarding Section 1
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="main-title">언제 어디서나,<br>내 손 안의 건강 비서<br>Health Mate</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Health Mate에 오신 것을 환영합니다!<br>건강 관리의 새로운 동반자를 만나보세요.</div>', 
                   unsafe_allow_html=True)
        
        st.image("online-learning0.svg", use_column_width=True)

    st.divider()

    # Onboarding Section 2
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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
        st.image("subscribe0.svg", use_column_width=True)
        
        st.markdown('<div class="section-title">맞춤형 정보 제공으로<br>쉽고, 자세하게 알려드려요.</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="section-text">여러분에게 가장 관련성 높은 정보를 쉽고 자세하게<br>'
                   '제공해 드릴게요.</div>', 
                   unsafe_allow_html=True)
        
        # Add "Start Chat" button
        st.markdown('<button class="start-chat stButton">시작하기</button>', unsafe_allow_html=True)

render_onboarding()
st.markdown('</div>', unsafe_allow_html=True)

# Scrollable chat section
st.markdown('<div class="chat-section">', unsafe_allow_html=True)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat messages
for message in reversed(st.session_state.messages):
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            display_text = message["content"].split("참고문헌:")
            st.markdown(display_text[0])
            if len(display_text) > 1:
                st.info('**참고문헌:**' + display_text[1])
        else:
            st.markdown(message["content"])

# Chat input
prompt = st.chat_input("질문을 입력하세요.")

if prompt:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Process the response
    api_url = "https://36a5-124-58-113-155.ngrok-free.app/chat/"
    request_uri = api_url + prompt
    
    try:
        if request_uri:
            response = requests.get(request_uri)
            if response.status_code == 200:
                data = response.json()
                if data:
                    response_text = data['message'].replace("~", "\~")
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                else:
                    st.write("답변을 얻지 못했습니다.")
            else:
                st.error("서버 응답 오류: " + str(response.status_code))
    except requests.exceptions.RequestException as e:
        st.error("서버와 통신할 수 없습니다: " + str(e))

st.markdown('</div></div>', unsafe_allow_html=True)
