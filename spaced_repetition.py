import streamlit as st

cards = [
    {"q": "pH formula?", "a": "-log[H+]"},
    {"q": "Molarity formula?", "a": "moles / liters"},
    {"q": "SN2 reaction type?", "a": "One-step substitution"},
]

st.title("🔁 Spaced Repetition System")

card = cards[0]

st.subheader(card["q"])
answer = st.text_input("Your answer")

if st.button("Check"):
    if answer.lower().strip() == card["a"].lower():
        st.success("Correct 🔥")
    else:
        st.error(f"Wrong. Answer: {card['a']}")