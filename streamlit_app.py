import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Health Mate",
    page_icon="🏥",
    layout="wide"
)

# CSS and JavaScript for slide functionality
st.markdown("""
<style>
    .main .block-container {
        max-width: 100%;
        padding-top: 0;
        padding-bottom: 0;
        overflow: hidden;
    }
    
    .slider-container {
        width: 300%;
        display: flex;
        transition: transform 0.5s ease;
    }
    
    .slide {
        width: 33.33%;
        flex-shrink: 0;
    }
    
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
    
    .nav-buttons {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 10px;
    }
    
    .nav-button {
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
    }
    
    .stChatFloatingInputContainer {
        position: fixed;
        bottom: 0;
        background: white;
        z-index: 101;
        width: 100%;
    }
</style>

<script>
function slide(direction) {
    const container = document.querySelector('.slider-container');
    let currentTransform = new WebKitCSSMatrix(window.getComputedStyle(container).transform).e;
    const slideWidth = document.querySelector('.slide').offsetWidth;
    
    if (direction === 'next' && currentTransform > -slideWidth * 2) {
        container.style.transform = `translateX(${currentTransform - slideWidth}px)`;
    } else if (direction === 'prev' && currentTransform < 0) {
        container.style.transform = `translateX(${currentTransform + slideWidth}px)`;
    }
}
</script>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

def main():
    st.markdown('<div class="slider-container">', unsafe_allow_html=True)
    
    # Slide 1
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">언제 어디서나,<br>내 손 안의 건강 비서<br>Health Mate</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Health Mate에 오신 것을 환영합니다!<br>건강 관리의 새로운 동반자를 만나보세요.</div>', unsafe_allow_html=True)
    st.image("online-learning0.svg", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Slide 2
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    st.image("group0.svg", use_column_width=True)
    st.markdown('<div class="section-title">궁금한 증상이나 질병에<br>대해 질문해주세요.</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-text">궁금한 증상이나 질병이 있다면 언제든지 질문해 주세요. 전문가 수준의 정보를 친절하게 안내해 드릴게요.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Slide 3
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    st.image("subscribe0.svg", use_column_width=True)
    st.markdown('<div class="section-title">맞춤형 정보 제공으로<br>쉽고, 자세하게 알려드려요.</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-text">여러분에게 가장 관련성 높은 정보를 쉽고 자세하게<br>제공해 드릴게요.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Navigation buttons
    st.markdown("""
    <div class="nav-buttons">
        <button class="nav-button" onclick="slide('prev')">이전</button>
        <button class="nav-button" onclick="slide('next')">다음</button>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# Display chat messages
for message in st.session_state.messages:
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
