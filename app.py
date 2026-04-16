import streamlit as st

st.set_page_config(page_title="Chemistry Master System v5", layout="wide")

st.title("🧪 Chemistry Master System v5")
st.write("Learn. Train. Test. Track. Pharma Path.")

page = st.sidebar.selectbox(
    "Choose Mode",
    ["Home", "Learn", "Spaced Repetition", "Exam Mode", "Progress", "Pharma Path"]
)

if page == "Home":
    st.header("Welcome")
    st.write("This is your full chemistry training system.")

elif page == "Learn":
    st.header("Learning Module")
    st.write("We will connect structured lessons here.")

elif page == "Spaced Repetition":
    st.header("Memory System")
    st.write("Anki-style flashcards coming next step.")

elif page == "Exam Mode":
    st.header("Timed Exams")
    st.write("We will add timer + scoring engine.")

elif page == "Progress":
    st.header("Your Progress")
    st.write("Graphs and analytics will show here.")

elif page == "Pharma Path":
    st.header("Pharmaceutical Chemistry Path")
    st.write("Drug chemistry, dosage, kinetics, solubility.")



