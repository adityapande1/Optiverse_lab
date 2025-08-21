import streamlit as st
from analyze import run as run_analyze
from trade import run as run_trade

st.sidebar.title("App Launcher")
app_choice = st.sidebar.radio("Choose an app:", ["Analyze", "Trade"])

if app_choice == "Analyze":
    run_analyze()
elif app_choice == "Trade":
    run_trade()
