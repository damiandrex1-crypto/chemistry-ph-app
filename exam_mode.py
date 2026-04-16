import streamlit as st
import time

st.title("🧠 Exam Mode")

time_limit = 30
start = st.button("Start Exam")

if start:
    st.write("Timer started: 30 seconds")

    for i in range(time_limit, 0, -1):
        st.write(f"Time left: {i} seconds")
        time.sleep(1)

    st.error("Time is up!")