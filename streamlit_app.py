import streamlit as st
import requests

# Page config should be at the top
st.set_page_config(
    page_title="Health Mate",
    page_icon="🏥",
    layout="wide"
)

# CSS to disable scrolling and show only col1 content
st.markdown("""
<style>
    /* Disable scrolling */
    .main .block-container {
        max-width: 100%;
        padding-top: 0;
        padding-bottom: 0;
        overflow: hidden;
    }
    
    /* Content styling */
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
    
    /* Hide col2 and col3 initially */
    .row-widget.stHorizontal > div:nth-child(2),
    .row-widget.stHorizontal > div:nth-child(3) {
        display: none;
    }
    
    /* Chat container */
    .stChatFloatingInputContainer {
        position: fixed;
        bottom: 0;
        background: white;
        z-index: 101;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

def main():
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown('<div class="main-title">언제 어디서나,<br>내 손 안의 건강 비서<br>Health Mate</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Health Mate에 오신 것을 환영합니다!<br>건강 관리의 새로운 동반자를 만나보세요.</div>', 
                   unsafe_allow_html=True)
        
        st.image("online-learning0.svg", use_column_width=True)

    with col2:
        st.image("group0.svg", use_column_width
