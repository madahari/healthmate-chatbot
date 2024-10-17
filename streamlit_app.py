import streamlit as st
import requests

# Page config should be at the top
st.set_page_config(
    page_title="Health Mate",
    page_icon="🏥",
    layout="wide"
)

# CSS to disable scrolling while maintaining the original layout
st.markdown("""
<style>
    /* Disable scrolling */
    .main .block-container {
        max-width: 100%;
        padding-top: 0;
        padding-bottom: 0;
        overflow: hidden;
        height: 100vh;
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
    .section-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .section-text {
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
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
    # Onboarding Section 1
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="main-title">언제 어디서나,<br>내 손 안의 건강 비서
