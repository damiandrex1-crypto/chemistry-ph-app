import streamlit as st

st.set_page_config(page_title="Chemistry Study Hub", layout="wide")

# ---------------- HEADER ----------------
st.title("🧪 Chemistry Study Hub")
st.caption("CHEM 1101 + CHEM 1201 Learning System")

# ---------------- SIDEBAR ----------------
course = st.sidebar.selectbox(
    "Navigate",
    ["Home", "CHEM 1101", "CHEM 1201", "Practice Quiz"]
)

# ---------------- HOME ----------------
if course == "Home":
    st.header("Welcome 👋")

    col1, col2, col3 = st.columns(3)

    col1.metric("Courses", "2")
    col2.metric("Modules", "13+")
    col3.metric("Mode", "Study")

    st.write("Use the sidebar to start learning chemistry step by step.")

# ---------------- CHEM 1101 ----------------
elif course == "CHEM 1101":
    st.header("📘 CHEM 1101 - General Chemistry 1")

    topic = st.selectbox("Select Topic", [
        "Atomic Structure",
        "Periodic Trends",
        "Bonding",
        "Stoichiometry",
        "Gases",
        "Thermochemistry",
        "Acids & Bases"
    ])

    st.subheader("📚 Lesson")

    lessons = {
        "Atomic Structure": "Atoms contain protons, neutrons, electrons. Electron configuration controls chemical behavior.",
        "Periodic Trends": "Across period: radius decreases. Down group: radius increases.",
        "Bonding": "Ionic = transfer of electrons. Covalent = sharing.",
        "Stoichiometry": "Use mole ratios from balanced equations.",
        "Gases": "PV = nRT ideal gas law.",
        "Thermochemistry": "Heat changes in reactions (exo vs endo).",
        "Acids & Bases": "pH = -log[H+]"
    }

    st.info(lessons[topic])

# ---------------- CHEM 1201 ----------------
elif course == "CHEM 1201":
    st.header("📘 CHEM 1201 - General Chemistry 2")

    topic = st.selectbox("Select Topic", [
        "Equilibrium",
        "Kinetics",
        "Thermodynamics",
        "Electrochemistry",
        "Solutions",
        "Buffers"
    ])

    st.subheader("📚 Lesson")

    lessons = {
        "Equilibrium": "Forward and reverse reactions balance at equilibrium.",
        "Kinetics": "Reaction rate depends on concentration and temperature.",
        "Thermodynamics": "ΔG = ΔH - TΔS determines spontaneity.",
        "Electrochemistry": "Redox reactions produce electricity.",
        "Solutions": "Solubility depends on polarity.",
        "Buffers": "Resist pH change using weak acid/base systems."
    }

    st.info(lessons[topic])

# ---------------- QUIZ ----------------
elif course == "Practice Quiz":
    st.header("🧠 Chemistry Quiz")

    col1, col2 = st.columns(2)

    with col1:
        q = st.radio("What is pH formula?", ["-log[H+]", "log[H+]", "H+/V"])

    with col2:
        st.write("Select answer and check below")

    if st.button("Check Answer"):
        if q == "-log[H+]":
            st.success("Correct 🔥")
        else:
            st.error("Wrong — correct answer is -log[H+]")



