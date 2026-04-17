import streamlit as st
import math
import random
import os
import PyPDF2

st.set_page_config(page_title="Chemistry Study Hub Pro", layout="wide")

# ---------------- SETUP ----------------
os.makedirs("slides", exist_ok=True)

# ---------------- NAVIGATION ----------------
page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "CHEM 1101", "CHEM 1201", "pH Tool", "Exam Mode", "Lecture Slides", "Study With Me"]
)

# ---------------- HOME ----------------
if page == "Home":
    st.title("🧪 Chemistry Study Hub Pro")
    st.write("Your full chemistry learning + exam + AI-style study system")

    col1, col2, col3 = st.columns(3)
    col1.metric("Courses", "2")
    col2.metric("Tools", "pH + Exams")
    col3.metric("Modes", "Study + Slides")

# ---------------- CHEM 1101 ----------------
elif page == "CHEM 1101":
    st.title("📘 CHEM 1101")

    topic = st.selectbox("Select Topic", [
        "Atomic Structure",
        "Periodic Trends",
        "Bonding",
        "Stoichiometry",
        "Gases",
        "Thermochemistry",
        "Acids & Bases"
    ])

    data = {
        "Atomic Structure": "Atoms contain protons, neutrons, electrons.",
        "Periodic Trends": "Across period radius decreases, down group increases.",
        "Bonding": "Ionic, covalent, metallic bonding.",
        "Stoichiometry": "Mole ratios from balanced equations.",
        "Gases": "PV = nRT gas law.",
        "Thermochemistry": "Heat changes in reactions.",
        "Acids & Bases": "Acids donate H+, bases accept H+."
    }

    st.subheader("Lesson")
    st.write(data[topic])

# ---------------- CHEM 1201 ----------------
elif page == "CHEM 1201":
    st.title("📘 CHEM 1201")

    topic = st.selectbox("Select Topic", [
        "Equilibrium",
        "Kinetics",
        "Thermodynamics",
        "Electrochemistry",
        "Solutions",
        "Buffers"
    ])

    data = {
        "Equilibrium": "Forward and reverse rates equal.",
        "Kinetics": "Reaction speed depends on conditions.",
        "Thermodynamics": "ΔG = ΔH - TΔS.",
        "Electrochemistry": "Redox reactions produce electricity.",
        "Solutions": "Like dissolves like.",
        "Buffers": "Resist pH changes."
    }

    st.subheader("Lesson")
    st.write(data[topic])

# ---------------- pH TOOL ----------------
elif page == "pH Tool":
    st.title("🧪 pH Calculator")

    mode = st.selectbox("Mode", ["Calculate pH", "Identify Acid/Base"])

    if mode == "Calculate pH":
        h = st.number_input("[H+] concentration", min_value=0.0000000001, format="%.10f")
        ph = -math.log10(h)

        st.success(f"pH = {ph:.2f}")

        if ph < 7:
            st.write("Acidic")
        elif ph > 7:
            st.write("Basic")
        else:
            st.write("Neutral")

    else:
        ph = st.number_input("Enter pH", 0.0, 14.0)

        if ph < 3:
            st.error("Strong Acid")
        elif ph < 7:
            st.warning("Weak Acid")
        elif ph == 7:
            st.info("Neutral")
        elif ph <= 11:
            st.success("Weak Base")
        else:
            st.success("Strong Base")

# ---------------- EXAM MODE ----------------
elif page == "Exam Mode":
    st.title("🧠 Exam Mode")

    questions = [
        ("pH formula?", ["-log[H+]", "log[H+]", "H+V"], "-log[H+]"),
        ("PV=nRT is?", ["Gas law", "Bonding", "Acid"], "Gas law"),
        ("Oxidation means?", ["Gain e-", "Lose e-", "Gain H+"], "Lose e-"),
    ]

    q, options, ans = random.choice(questions)

    st.subheader(q)
    choice = st.radio("Answer", options)

    if st.button("Check"):
        if choice == ans:
            st.success("Correct 🔥")
        else:
            st.error(f"Wrong. Answer: {ans}")

# ---------------- LECTURE SLIDES ----------------
elif page == "Lecture Slides":
    st.title("📚 Lecture Slides System")

    subject = st.selectbox("Course", ["CHEM 1101", "CHEM 1201"])

    uploaded = st.file_uploader("Upload PDF Slides", type=["pdf"])

    if uploaded:
        file_path = f"slides/{subject.replace(' ', '').lower()}.pdf"
        with open(file_path, "wb") as f:
            f.write(uploaded.getbuffer())
        st.success("Uploaded ✔")

    file_map = {
        "CHEM 1101": "slides/chem1101.pdf",
        "CHEM 1201": "slides/chem1201.pdf"
    }

    path = file_map[subject]

    if os.path.exists(path):
        st.success("Slides available ✔")
        with open(path, "rb") as f:
            st.download_button("Download Slides", f, file_name=path)
    else:
        st.warning("No slides uploaded yet")

# ---------------- STUDY WITH ME ----------------
elif page == "Study With Me":
    st.title("🧠 Study With Me Mode")

    subject = st.selectbox("Course", ["CHEM 1101", "CHEM 1201"])

    file_map = {
        "CHEM 1101": "slides/chem1101.pdf",
        "CHEM 1201": "slides/chem1201.pdf"
    }

    path = file_map[subject]

    def extract_text(pdf_path):
        text = ""
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""
        return text

    text = extract_text(path)

    if text.strip() == "":
        st.warning("No readable slides found.")
    else:
        mode = st.selectbox("Mode", ["Summary", "Quiz Me", "Teach Back"])

        if mode == "Summary":
            st.subheader("Summary")
            st.write(text[:2000])

        elif mode == "Quiz Me":
            st.subheader("Quiz")

            sentences = text.split(".")
            q = random.choice(sentences)

            st.info(f"Explain: {q.strip()}")

            answer = st.text_input("Your answer")

            if st.button("Check"):
                if len(answer) > 10:
                    st.success("Good effort 🔥")
                else:
                    st.error("Write more detail")

        elif mode == "Teach Back":
            st.subheader("Teach Back")

            user = st.text_area("Explain the topic in your own words")

            if st.button("Review"):
                if len(user) > 20:
                    st.success("Strong explanation 🔥")
                else:
                    st.warning("Add more detail like you're teaching someone")