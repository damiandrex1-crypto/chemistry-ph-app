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

# ---------------- DATA ----------------
chem_1101 = {
    "Atomic Structure": {
        "definition": "Atoms are made of protons, neutrons, and electrons.",
        "explanation": "Protons determine element identity. Neutrons affect mass. Electrons control bonding.",
        "example": "Carbon has 6 protons and 6 electrons.",
        "exam_tip": "Electrons determine chemical behavior."
    },
    "Periodic Trends": {
        "definition": "Patterns in the periodic table.",
        "explanation": "Across period: radius decreases. Down group: radius increases.",
        "example": "Na is larger than Cl.",
        "exam_tip": "Use nuclear charge and shielding."
    },
    "Bonding": {
        "definition": "How atoms form compounds.",
        "explanation": "Ionic = transfer, Covalent = sharing, Metallic = electron sea.",
        "example": "NaCl is ionic.",
        "exam_tip": "Check electronegativity difference."
    },
    "Stoichiometry": {
        "definition": "Mole relationships in reactions.",
        "explanation": "Balanced equations give mole ratios.",
        "example": "2H2 + O2 → 2H2O",
        "exam_tip": "Always convert to moles first."
    },
    "Gases": {
        "definition": "Gas behavior follows PV=nRT.",
        "explanation": "Pressure, volume, temperature, moles relationship.",
        "example": "Hot gas increases pressure.",
        "exam_tip": "Use Kelvin only."
    },
    "Thermochemistry": {
        "definition": "Energy changes in reactions.",
        "explanation": "Exothermic releases heat. Endothermic absorbs heat.",
        "example": "Burning fuel releases heat.",
        "exam_tip": "ΔH negative = exothermic."
    },
    "Acids & Bases": {
        "definition": "Acids donate H+, bases accept H+.",
        "explanation": "pH scale measures acidity.",
        "example": "HCl is strong acid.",
        "exam_tip": "pH < 7 is acidic."
    }
}

chem_1201 = {
    "Equilibrium": {
        "definition": "Forward and reverse reactions occur at same rate.",
        "explanation": "System is dynamic but stable.",
        "example": "N2 + 3H2 ⇌ 2NH3",
        "exam_tip": "Le Chatelier principle."
    },
    "Kinetics": {
        "definition": "Reaction speed.",
        "explanation": "Depends on temperature and concentration.",
        "example": "Heat increases rate.",
        "exam_tip": "Rate ≠ equilibrium."
    },
    "Thermodynamics": {
        "definition": "Predicts spontaneity.",
        "explanation": "ΔG = ΔH - TΔS",
        "example": "Ice melting.",
        "exam_tip": "Negative ΔG = spontaneous."
    },
    "Electrochemistry": {
        "definition": "Redox reactions produce electricity.",
        "explanation": "Oxidation = loss, reduction = gain.",
        "example": "Batteries use redox.",
        "exam_tip": "OIL RIG."
    },
    "Solutions": {
        "definition": "Homogeneous mixtures.",
        "explanation": "Like dissolves like.",
        "example": "Salt in water.",
        "exam_tip": "Temperature affects solubility."
    },
    "Buffers": {
        "definition": "Resist pH change.",
        "explanation": "Weak acid + conjugate base system.",
        "example": "Blood buffer system.",
        "exam_tip": "Henderson-Hasselbalch equation."
    }
}

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

    topic = st.selectbox("Select Topic", list(chem_1101.keys()))
    data = chem_1101[topic]

    st.subheader(topic)
    st.write("**Definition:**", data["definition"])
    st.write("**Explanation:**", data["explanation"])
    st.write("**Example:**", data["example"])
    st.write("**Exam Tip:**", data["exam_tip"])

# ---------------- CHEM 1201 ----------------
elif course == "CHEM 1201":
    st.header("📘 CHEM 1201 - General Chemistry 2")

    topic = st.selectbox("Select Topic", list(chem_1201.keys()))
    data = chem_1201[topic]

    st.subheader(topic)
    st.write("**Definition:**", data["definition"])
    st.write("**Explanation:**", data["explanation"])
    st.write("**Example:**", data["example"])
    st.write("**Exam Tip:**", data["exam_tip"])

# ---------------- PRACTICE QUIZ ----------------
elif course == "Practice Quiz":
    st.header("🧪 Practice Quiz")

    questions = [
        {
            "question": "What is the charge of a proton?",
            "options": ["negative", "neutral", "positive", "zero"],
            "answer": "positive"
        },
        {
            "question": "pH less than 7 means the solution is:",
            "options": ["basic", "acidic", "neutral", "salt"],
            "answer": "acidic"
        },
        {
            "question": "PV = nRT is used for:",
            "options": ["solids", "liquids", "gases", "metals"],
            "answer": "gases"
        },
        {
            "question": "OIL RIG stands for:",
            "options": [
                "oxidation is loss, reduction is gain",
                "oxygen is loss, iron is gain",
                "oxidation is liquid, reduction is gas",
                "none"
            ],
            "answer": "oxidation is loss, reduction is gain"
        }
    ]

    score = 0

    for i, q in enumerate(questions):
        st.write(f"**{i+1}. {q['question']}**")

        choice = st.radio(
            f"Select answer {i+1}",
            q["options"],
            key=i
        )

        if choice == q["answer"]:
            score += 1

    if st.button("Submit Quiz"):
        st.success(f"Your Score: {score} / {len(questions)}")

        if score == len(questions):
            st.balloons()