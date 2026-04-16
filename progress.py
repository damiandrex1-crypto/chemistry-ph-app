import streamlit as st

st.title("📊 Progress Analytics")

correct = 7
wrong = 3

st.metric("Correct Answers", correct)
st.metric("Wrong Answers", wrong)

st.bar_chart({
    "Correct": [correct],
    "Wrong": [wrong]
})