import streamlit as st
from analyze import run as run_analyze
from trade import run as run_trade

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Analyze"

# --- Top navigation bar ---
st.markdown(
    """
    <style>
    .topnav {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .topnav button {
        background-color: #f0f2f6;
        border: 2px solid #ccc;
        border-radius: 8px;
        padding: 10px 20px;
        margin: 0 10px;
        cursor: pointer;
        font-size: 16px;
        font-weight: 500;
    }
    .topnav button:hover {
        background-color: #e6e6e6;
    }
    .active {
        background-color: #4CAF50 !important;
        color: white !important;
        border-color: #4CAF50 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Create buttons ---
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Analyze", key="btn_analyze"):
        st.session_state.page = "Analyze"
with col2:
    if st.button("Trade", key="btn_trade"):
        st.session_state.page = "Trade"

# Highlight active button
if st.session_state.page == "Analyze":
    st.markdown("<style>#btn_analyze{background-color:#4CAF50;color:white;border-color:#4CAF50;}</style>", unsafe_allow_html=True)
elif st.session_state.page == "Trade":
    st.markdown("<style>#btn_trade{background-color:#4CAF50;color:white;border-color:#4CAF50;}</style>", unsafe_allow_html=True)

# --- Render selected page ---
if st.session_state.page == "Analyze":
    run_analyze()
elif st.session_state.page == "Trade":
    run_trade()
