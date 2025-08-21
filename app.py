import streamlit as st
import subprocess
import sys
import os
import webbrowser

# Sidebar selection
st.sidebar.title("App Launcher")
app_choice = st.sidebar.radio("Choose an app:", ["Analyze", "Trade"])

# Button to launch app
if st.sidebar.button("Open App"):
    if app_choice == "Analyze":
        script = "analyze.py"
        port = 8502
    elif app_choice == "Trade":
        script = "trade.py"
        port = 8503
    else:
        script = None

    if script:
        # Run new streamlit process
        subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", script, f"--server.port={port}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )

        # Open in browser
        webbrowser.open(f"http://localhost:{port}")
        st.sidebar.success(f"Launched {script} on port {port}")
