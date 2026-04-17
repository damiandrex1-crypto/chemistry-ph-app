import streamlit as st
import math
import random
import base64

st.set_page_config(page_title="Chemistry Study Hub", layout="wide")

# ---------------- NAVIGATION ----------------
course = st.sidebar.selectbox(
    "Navigate",
    ["Home", "CHEM 1101", "CHEM 1201", "pH Tool", "Exam Mode", "Lecture Slides"]
)

# ---------------- HOME ----------------
if course == "Home":
    st.title("🧪 Chemistry Study Hub")
    st.write("CHEM 1101 + CHEM 1201 + Tools + Exams + Lecture Slides")

    col1, col2, col3 = st.columns(3)
    col1.metric("Courses", "2")
    col2.metric("Tools", "pH + Exams")
    col3.metric("Feature", "Slides Viewer")

# ---------------- CHEM 1101 ----------------
elif course == "CHEM 1101":
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

    lessons = {
        "Atomic Structure": {
            "definition": "Atoms consist of protons, neutrons, electrons.",
            "explanation": "Protons define element identity, electrons control bonding.",
            "example": "Carbon has 6 protons.",
            "exam_tip": "Electron configuration = reactivity."
        },

        "Periodic Trends": {
            "definition": "Patterns in periodic table properties.",
            "explanation": "Across: radius decreases. Down: increases.",
            "example": "Na larger than Cl.",
            "exam_tip": "Mention shielding effect."
        },

        "Bonding": {
            "definition": "How atoms connect.",
            "explanation": "Ionic, covalent, metallic bonding.",
            "example": "NaCl ionic.",
            "exam_tip": "Use electronegativity."
        },

        "Stoichiometry": {
            "definition": "Mole relationships in reactions.",
            "explanation": "Convert grams → moles → ratios.",
            "example": "2H2 + O2 → 2H2O",
            "exam_tip": "Balance first."
        },

        "Gases": {
            "definition": "PV=nRT relationships.",
            "explanation": "Gas behavior changes with T, P, V.",
            "example": "Hot air expands.",
            "exam_tip": "Kelvin only."
        },

        "Thermochemistry": {
            "definition": "Energy in reactions.",
            "explanation": "Exothermic vs endothermic.",
            "example": "Burning fuel.",
            "exam_tip": "ΔH sign matters."
        },

        "Acids & Bases": {
            "definition": "H+ donors and acceptors.",
            "explanation": "pH scale measures acidity.",
            "example": "HCl strong acid.",
            "exam_tip": "pH < 7 acid."
        }
    }

    d = lessons[topic]

    st.subheader("Definition")
    st.write(d["definition"])

    st.subheader("Explanation")
    st.write(d["explanation"])

    st.subheader("Example")
    st.write(d["example"])

    st.subheader("Exam Tip")
    st.warning(d["exam_tip"])

# ---------------- CHEM 1201 ----------------
elif course == "CHEM 1201":
    st.title("📘 CHEM 1201")

    topic = st.selectbox("Select Topic", [
        "Equilibrium",
        "Kinetics",
        "Thermodynamics",
        "Electrochemistry",
        "Solutions",
        "Buffers"
    ])

    lessons = {
        "Equilibrium": {
            "definition": "Forward and reverse rates equal.",
            "explanation": "Dynamic balance of reactions.",
            "example": "N2 + 3H2 ⇌ 2NH3",
            "exam_tip": "Le Chatelier's principle."
        },

        "Kinetics": {
            "definition": "Reaction speed study.",
            "explanation": "Rate depends on concentration and temperature.",
            "example": "Higher temp = faster reaction.",
            "exam_tip": "Rate ≠ equilibrium."
        },

        "Thermodynamics": {
            "definition": "Spontaneity prediction.",
            "explanation": "ΔG = ΔH - TΔS.",
            "example": "Ice melting.",
            "exam_tip": "ΔG negative = spontaneous."
        },

        "Electrochemistry": {
            "definition": "Redox and electricity.",
            "explanation": "Oxidation loss, reduction gain.",
            "example": "Batteries.",
            "exam_tip": "OIL RIG."
        },

        "Solutions": {
            "definition": "Homogeneous mixtures.",
            "explanation": "Like dissolves like.",
            "example": "Salt water.",
            "exam_tip": "Polarity matters."
        },

        "Buffers": {
            "definition": "Resist pH changes.",
            "explanation": "Weak acid + base system.",
            "example": "Blood buffer.",
            "exam_tip": "H-H equation."
        }
    }

    d = lessons[topic]

    st.subheader("Definition")
    st.write(d["definition"])

    st.subheader("Explanation")
    st.write(d["explanation"])

    st.subheader("Example")
    st.write(d["example"])

    st.subheader("Exam Tip")
    st.warning(d["exam_tip"])

# ---------------- pH TOOL ----------------
elif course == "pH Tool":
    st.title("🧪 pH Tool")

    mode = st.selectbox("Mode", ["Calculator", "Identifier"])

    if mode == "Calculator":
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
        ph = st.number_input("Enter pH", min_value=0.0, max_value=14.0)

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
elif course == "Exam Mode":
    st.title("🧠 Exam Mode")

    questions = [
        {"q": "pH formula?", "options": ["-log[H+]", "log[H+]", "H+V"], "answer": "-log[H+]"},
        {"q": "PV=nRT is?", "options": ["Gas law", "Bonding", "Acid"], "answer": "Gas law"},
        {"q": "Oxidation?", "options": ["Gain e-", "Lose e-", "Gain H+"], "answer": "Lose e-"},
    ]

    q = random.choice(questions)

    st.subheader(q["q"])
    choice = st.radio("Answer", q["options"])

    if st.button("Check"):
        if choice == q["answer"]:
            st.success("Correct 🔥")
        else:
            st.error("Wrong")

# ---------------- LECTURE SLIDES (PDF VIEWER) ----------------
elif course == "Lecture Slides":
    st.title("📚 Lecture Slides Viewer")

    subject = st.selectbox("Course", ["CHEM 1101", "CHEM 1201"])

    def show_pdf(file_path):
        try:
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
        except:
            st.warning("PDF not found. Put file in /slides folder.")

    if subject == "CHEM 1101":
        st.subheader("CHEM 1101 Slides")
        show_pdf("slides/chem1101.pdf")

    if subject == "CHEM 1201":
        st.subheader("CHEM 1201 Slides")
        show_pdf("slides/chem1201.pdf")