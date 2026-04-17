import streamlit as st
import math

st.set_page_config(page_title="Chemistry Study Hub", layout="wide")

# ---------------- HEADER ----------------
st.title("🧪 Chemistry Study Hub")
st.caption("CHEM 1101 + CHEM 1201 + Tools System")

# ---------------- NAVIGATION ----------------
course = st.sidebar.selectbox(
    "Navigate",
    ["Home", "CHEM 1101", "CHEM 1201", "pH Tool"]
)

# ---------------- HOME ----------------
if course == "Home":
    st.header("Welcome 👋")

    col1, col2, col3 = st.columns(3)

    col1.metric("Courses", "2")
    col2.metric("Topics", "13+")
    col3.metric("Tools", "pH Calculator")

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

    lessons = {
        "Atomic Structure": {
            "definition": "Atoms are made of protons, neutrons, electrons.",
            "explanation": "Protons define element. Electrons control bonding. Neutrons affect mass.",
            "example": "Carbon has 6 protons and 6 electrons.",
            "exam_tip": "Electron configuration determines reactivity."
        },

        "Periodic Trends": {
            "definition": "Trends explain atomic changes in periodic table.",
            "explanation": "Across period: radius decreases. Down group: radius increases.",
            "example": "Na is larger than Cl in same period.",
            "exam_tip": "Always mention nuclear charge + shielding."
        },

        "Bonding": {
            "definition": "Bonding is how atoms combine.",
            "explanation": "Ionic = transfer, Covalent = sharing, Metallic = electron sea.",
            "example": "NaCl is ionic, H2O is covalent.",
            "exam_tip": "Use electronegativity difference."
        },

        "Stoichiometry": {
            "definition": "Uses mole ratios from balanced equations.",
            "explanation": "Convert grams → moles → ratios.",
            "example": "2H2 + O2 → 2H2O",
            "exam_tip": "Balance equation first."
        },

        "Gases": {
            "definition": "Gas behavior follows PV = nRT.",
            "explanation": "Pressure, volume, temperature relationships.",
            "example": "Hot air expands.",
            "exam_tip": "Temperature must be in Kelvin."
        },

        "Thermochemistry": {
            "definition": "Study of energy changes.",
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
    st.header("📘 CHEM 1201 - General Chemistry 2")

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
            "definition": "Forward and reverse reactions balance.",
            "explanation": "Dynamic equilibrium where rates are equal.",
            "example": "N2 + 3H2 ⇌ 2NH3",
            "exam_tip": "Use Le Chatelier’s principle."
        },

        "Kinetics": {
            "definition": "Study of reaction speed.",
            "explanation": "Rate depends on concentration and temperature.",
            "example": "Higher temperature = faster reaction.",
            "exam_tip": "Rate ≠ equilibrium."
        },

        "Thermodynamics": {
            "definition": "Predicts if reactions are spontaneous.",
            "explanation": "ΔG = ΔH - TΔS.",
            "example": "Ice melting at room temp.",
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
            "explanation": "Weak acid + conjugate base system.",
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
    st.header("🧪 pH Calculator + Acid/Base Identifier")

    mode = st.selectbox("Mode", ["pH Calculator", "Acid/Base Identifier"])

    if mode == "pH Calculator":
        h = st.number_input("[H+] concentration (mol/L)", min_value=0.0000000001, format="%.10f")

        if h > 0:
            ph = -math.log10(h)
            st.success(f"pH = {ph:.2f}")

            if ph < 7:
                st.write("🔴 Acidic solution")
            elif ph > 7:
                st.write("🟢 Basic solution")
            else:
                st.write("⚪ Neutral solution")

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
