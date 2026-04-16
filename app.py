import streamlit as st
import math

st.set_page_config(page_title="Chemistry Study Hub", layout="wide")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "Tools", "Quiz", "Pharma Mode"])

# ---------------- HOME ----------------
if page == "Home":
    st.title("🧪 Chemistry Study Hub")
    st.subheader("A real interactive learning system")

    col1, col2, col3 = st.columns(3)

    col1.metric("Modules", "4")
    col2.metric("Tools", "3")
    col3.metric("Mode", "Learning")

    st.write("Use the sidebar to navigate.")

# ---------------- TOOLS ----------------
elif page == "Tools":
    st.title("⚗️ Chemistry Tools")

    tool = st.selectbox("Choose Tool", ["pH Calculator", "Molarity", "Dilution"])

    if tool == "pH Calculator":
        h = st.number_input("[H+] concentration", min_value=0.0000001)
        if h > 0:
            st.success(f"pH = {-math.log10(h):.2f}")

    elif tool == "Molarity":
        m = st.number_input("Moles")
        v = st.number_input("Volume (L)")
        if v > 0:
            st.success(f"M = {m/v:.3f}")

    elif tool == "Dilution":
        c1 = st.number_input("C1")
        v1 = st.number_input("V1")
        c2 = st.number_input("C2")
        if c2 > 0:
            st.success(f"V2 = {(c1*v1)/c2:.3f}")

# ---------------- QUIZ ----------------
elif page == "Quiz":
    st.title("🧠 Quick Quiz")

    q = st.radio("What is pH formula?", ["-log[H+]", "log[H+]", "H+/V"])

    if st.button("Check"):
        if q == "-log[H+]":
            st.success("Correct 🔥")
        else:
            st.error("Wrong")

# ---------------- PHARMA ----------------
elif page == "Pharma Mode":
    st.title("💊 Pharma Chemistry Path")

    st.write("""
    - Drug solubility depends on pH
    - Weak acids behave differently in body
    - Henderson-Hasselbalch equation is key
    """)



