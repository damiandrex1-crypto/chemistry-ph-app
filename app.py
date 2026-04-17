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
        "explanation": "Protons determine identity. Neutrons affect mass. Electrons control bonding.",
        "example": "Carbon has 6 protons and 6 electrons.",
        "exam_tip": "Electrons determine chemical behavior."
    },
    "Periodic Trends": {
        "definition": "Trends describe patterns in the periodic table.",
        "explanation": "Across period: radius decreases. Down group: radius increases.",
        "example": "Na is larger than Cl.",
        "exam_tip": "Use nuclear charge + shielding."
    },
    "Bonding": {
        "definition": "How atoms form compounds.",
        "explanation": "Ionic = transfer. Covalent = sharing. Metallic = electron sea.",
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
        "definition": "Gas behavior uses PV=nRT.",
        "explanation": "Pressure, volume, temperature, moles relationship.",
        "example": "Hot gas increases pressure.",
        "exam_tip": "Use Kelvin only."
    },
    "Thermochemistry": {
        "definition": "Energy changes in reactions.",
        "explanation": "Exothermic releases heat. Endothermic absorbs heat.",
        "example": "Burning fuel.",
        "exam_tip": "ΔH negative = exothermic."
    },
    "Acids & Bases": {
        "definition": "Acids donate H+, bases accept H+.",
        "explanation": "pH measures acidity. Strong acids fully dissociate.",
        "example": "HCl is strong acid.",
        "exam_tip": "pH < 7 is acidic."
    }
}

chem_1201 = {
    "Equilibrium": {
        "definition": "Forward and reverse reactions occur at same rate.",
        "explanation": "Concentrations stay constant but reactions continue.",
        "example": "N2 + 3H2 ⇌ 2NH3",
        "exam_tip": "Le Chatelier principle."
    },
    "Kinetics": {
        "definition": "Reaction speed.",
        "explanation": "Depends on temperature, concentration, catalysts.",
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
        "example": "Batteries.",
        "exam_tip": "OIL RIG."
    },
    "Solutions": {
        "definition": "Homogeneous mixtures.",
        "explanation": "Like dissolves like.",
        "example": "Salt in water.",
        "exam_tip": "Temperature affects solubility."
    },
    "Buffers": {
        "definition": "Resist pH changes.",
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