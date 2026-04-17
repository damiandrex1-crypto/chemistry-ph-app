import streamlit as st
import math
import random

st.set_page_config(page_title="Chemistry Study Hub", layout="wide")

# ---------------- NAVIGATION ----------------
course = st.sidebar.selectbox(
    "Navigate",
    ["Home", "CHEM 1101", "CHEM 1201", "pH Tool", "Exam Mode"]
)

# ---------------- HOME ----------------
if course == "Home":
    st.title("🧪 Chemistry Study Hub")
    st.write("Full CHEM 1101 + CHEM 1201 learning + tools + exams")

    col1, col2, col3 = st.columns(3)

    col1.metric("Courses", "2")
    col2.metric("Tools", "pH Calculator")
    col3.metric("Mode", "Exam Ready")

# ---------------- CHEM 1101 ----------------
elif course == "CHEM 1101":
    st.title("📘 CHEM 1101 - General Chemistry 1")

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
            "definition": "Atoms consist of protons, neutrons, and electrons.",
            "explanation": "Protons define element, electrons control bonding, neutrons affect mass number.",
            "example": "Carbon has 6 protons and 6 electrons.",
            "exam_tip": "Electron configuration determines reactivity."
        },

        "Periodic Trends": {
            "definition": "Trends describe periodic changes in properties.",
            "explanation": "Across period: radius decreases. Down group: radius increases.",
            "example": "Cl is smaller than Na.",
            "exam_tip": "Mention nuclear charge + shielding effect."
        },

        "Bonding": {
            "definition": "Atoms bond to achieve stability.",
            "explanation": "Ionic = transfer, covalent = sharing, metallic = electron sea.",
            "example": "NaCl ionic, H2O covalent.",
            "exam_tip": "Use electronegativity difference."
        },

        "Stoichiometry": {
            "definition": "Uses mole ratios from equations.",
            "explanation": "Convert grams → moles → ratios.",
            "example": "2H2 + O2 → 2H2O",
            "exam_tip": "Balance equation first."
        },

        "Gases": {
            "definition": "Gas behavior follows PV = nRT.",
            "explanation": "Pressure, volume, temperature relationships.",
            "example": "Hot air expands.",
            "exam_tip": "Temperature in Kelvin."
        },

        "Thermochemistry": {
            "definition": "Study of heat energy changes.",
            "explanation": "Exothermic releases heat, endothermic absorbs heat.",
            "example": "Burning fuel releases energy.",
            "exam_tip": "ΔH negative = exothermic."
        },

        "Acids & Bases": {
            "definition": "Acids donate H+, bases accept H+.",
            "explanation": "pH measures acidity level.",
            "example": "HCl is strong acid.",
            "exam_tip": "pH < 7 acidic, > 7 basic."
        }
    }

    data = lessons[topic]

    st.subheader("📌 Definition")
    st.write(data["definition"])

    st.subheader("🧠 Explanation")
    st.write(data["explanation"])

    st.subheader("🧪 Example")
    st.write(data["example"])

    st.subheader("⚠️ Exam Tip")
    st.warning(data["exam_tip"])

# ---------------- CHEM 1201 ----------------
elif course == "CHEM 1201":
    st.title("📘 CHEM 1201 - General Chemistry 2")

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
            "definition": "Forward and reverse reactions are balanced.",
            "explanation": "Dynamic equilibrium occurs when rates are equal.",
            "example": "N2 + 3H2 ⇌ 2NH3",
            "exam_tip": "Use Le Chatelier’s principle."
        },

        "Kinetics": {
            "definition": "Studies reaction speed.",
            "explanation": "Depends on concentration, temperature, catalysts.",
            "example": "Higher temperature increases rate.",
            "exam_tip": "Rate ≠ equilibrium."
        },

        "Thermodynamics": {
            "definition": "Predicts if reaction is spontaneous.",
            "explanation": "ΔG = ΔH - TΔS.",
            "example": "Ice melting.",
            "exam_tip": "Negative ΔG = spontaneous."
        },

        "Electrochemistry": {
            "definition": "Redox reactions produce electricity.",
            "explanation": "Oxidation = loss, reduction = gain.",
            "example": "Batteries.",
            "exam_tip": "OIL RIG rule."
        },

        "Solutions": {
            "definition": "Homogeneous mixtures.",
            "explanation": "Like dissolves like.",
            "example": "Salt in water.",
            "exam_tip": "Polarity matters."
        },

        "Buffers": {
            "definition": "Resist pH change.",
            "explanation": "Weak acid + conjugate base.",
            "example": "Blood buffer system.",
            "exam_tip": "Henderson-Hasselbalch equation."
        }
    }

    data = lessons[topic]

    st.subheader("📌 Definition")
    st.write(data["definition"])

    st.subheader("🧠 Explanation")
    st.write(data["explanation"])

    st.subheader("🧪 Example")
    st.write(data["example"])

    st.subheader("⚠️ Exam Tip")
    st.warning(data["exam_tip"])

# ---------------- pH TOOL ----------------
elif course == "pH Tool":
    st.title("🧪 pH Calculator + Acid/Base Identifier")

    mode = st.selectbox("Mode", ["pH Calculator", "Acid/Base Identifier"])

    if mode == "pH Calculator":
        h = st.number_input("[H+] concentration (mol/L)", min_value=0.0000000001, format="%.10f")

        if h > 0:
            ph = -math.log10(h)
            st.success(f"pH = {ph:.2f}")

            if ph < 7:
                st.write("🔴 Acidic")
            elif ph > 7:
                st.write("🟢 Basic")
            else:
                st.write("⚪ Neutral")

    elif mode == "Acid/Base Identifier":
        ph = st.number_input("Enter pH value", min_value=0.0, max_value=14.0)

        if ph < 3:
            st.error("Strong Acid → HCl, HNO3, H2SO4")
        elif ph < 7:
            st.warning("Weak Acid → CH3COOH, H2CO3")
        elif ph == 7:
            st.info("Neutral → Water")
        elif ph <= 11:
            st.success("Weak Base → NH3, NaHCO3")
        else:
            st.success("Strong Base → NaOH, KOH")

# ---------------- EXAM MODE ----------------
elif course == "Exam Mode":
    st.title("🧠 Chemistry Exam Mode")

    questions = [
        {
            "q": "What is pH formula?",
            "options": ["-log[H+]", "log[H+]", "H+/V"],
            "answer": "-log[H+]"
        },
        {
            "q": "What does PV=nRT represent?",
            "options": ["Gas law", "Bonding", "Acid rule"],
            "answer": "Gas law"
        },
        {
            "q": "Oxidation means?",
            "options": ["Gain electrons", "Lose electrons", "Gain protons"],
            "answer": "Lose electrons"
        },
        {
            "q": "What is equilibrium?",
            "options": ["One-way reaction", "Forward=reverse rate", "No reaction"],
            "answer": "Forward=reverse rate"
        }
    ]

    question = random.choice(questions)

    st.subheader(question["q"])

    choice = st.radio("Choose answer", question["options"])

    if st.button("Check Answer"):
        if choice == question["answer"]:
            st.success("Correct 🔥")
        else:
            st.error(f"Wrong. Correct answer: {question['answer']}")
