import streamlit as st
import time

st.set_page_config(page_title="Chemistry Study Hub", layout="wide")

# ---------------- HEADER ----------------
st.title("🧪 Chemistry Study Hub")
st.caption("CHEM 1101 + CHEM 1201 - Exam Prep System")

# ---------------- SIDEBAR ----------------
course = st.sidebar.selectbox(
    "Navigate",
    ["Home", "CHEM 1101", "CHEM 1201", "Practice Quiz", "Exam Mode"]
)

# ---------------- DATA ----------------
chem_1101 = {
    "Atomic Structure": "Atoms contain protons, neutrons, electrons.",
    "Stoichiometry": "Mole ratios in reactions.",
    "Gases": "PV=nRT gas law.",
    "Bonding": "Ionic, covalent, metallic bonding."
}

chem_1201 = {
    "Equilibrium": "Forward = reverse reaction rate.",
    "Kinetics": "Reaction speed depends on conditions.",
    "Thermodynamics": "ΔG = ΔH - TΔS",
    "Electrochemistry": "Redox reactions produce electricity."
}

# ---------------- HOME ----------------
if course == "Home":
    st.header("Welcome 👋")

    col1, col2, col3 = st.columns(3)
    col1.metric("Courses", "2")
    col2.metric("Mode", "Exam Prep")
    col3.metric("System", "Active")

    st.write("Use this app to study, test yourself, and prepare for exams.")

# ---------------- CHEM 1101 ----------------
elif course == "CHEM 1101":
    st.header("📘 CHEM 1101")

    topic = st.selectbox("Select Topic", list(chem_1101.keys()))
    st.write(chem_1101[topic])

# ---------------- CHEM 1201 ----------------
elif course == "CHEM 1201":
    st.header("📘 CHEM 1201")

    topic = st.selectbox("Select Topic", list(chem_1201.keys()))
    st.write(chem_1201[topic])

# ---------------- PRACTICE QUIZ ----------------
elif course == "Practice Quiz":
    st.header("🧪 Practice Quiz")

    questions = [
        {
            "q": "What is the charge of a proton?",
            "options": ["negative", "neutral", "positive", "zero"],
            "answer": "positive"
        },
        {
            "q": "pH < 7 means?",
            "options": ["basic", "acidic", "neutral", "salt"],
            "answer": "acidic"
        },
        {
            "q": "PV=nRT is used for?",
            "options": ["solids", "liquids", "gases", "plasma"],
            "answer": "gases"
        }
    ]

    score = 0

    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {q['q']}**")
        choice = st.radio("Choose:", q["options"], key=f"quiz_{i}")

        if choice == q["answer"]:
            score += 1
        else:
            if "wrong_answers" not in st.session_state:
                st.session_state.wrong_answers = []
            st.session_state.wrong_answers.append(q["q"])

    if st.button("Submit Quiz"):
        st.success(f"Score: {score}/{len(questions)}")

# ---------------- EXAM MODE (STEP 1) ----------------
elif course == "Exam Mode":
    st.header("🧪 Exam Mode (Timed Test)")

    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()

    questions = [
        {"q": "What is charge of proton?", "options": ["negative","neutral","positive","zero"], "answer": "positive"},
        {"q": "PV=nRT applies to?", "options": ["solids","liquids","gases","metals"], "answer": "gases"},
        {"q": "pH < 7 means?", "options": ["basic","acidic","neutral","salt"], "answer": "acidic"}
    ]

    elapsed = int(time.time() - st.session_state.start_time)
    remaining = 300 - elapsed

    st.warning(f"Time left: {remaining} seconds")

    if remaining <= 0:
        st.error("Time is up!")

    score = 0

    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {q['q']}**")
        choice = st.radio("Answer:", q["options"], key=f"exam_{i}")

        if choice == q["answer"]:
            score += 1

    if st.button("Submit Exam"):
        st.success(f"Final Score: {score}/{len(questions)}")

        if score >= len(questions) * 0.75:
            st.balloons()
            st.success("Exam Ready Level 🔥")

# ---------------- WEAK AREA TRACKER (STEP 2) ----------------
    st.subheader("📊 Weak Areas")

    if "wrong_answers" in st.session_state:
        if len(st.session_state.wrong_answers) > 0:
            for w in st.session_state.wrong_answers:
                st.write("•", w)
        else:
            st.info("No weak areas yet.")
    else:
        st.info("Take quizzes first.")

# ---------------- FOCUS MODE (STEP 3) ----------------
    st.subheader("🎯 Focus Mode")

    focus = st.selectbox("Pick weak topic focus", [
        "Atomic Structure",
        "Stoichiometry",
        "Gases",
        "Equilibrium",
        "Kinetics"
    ])

    st.info(f"Focus on: {focus}")
