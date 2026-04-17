import streamlit as st
import math

st.title("🧪 pH Calculator + Acid/Base Identifier")

mode = st.selectbox("Mode", ["pH Calculator", "Acid/Base Identifier"])

if mode == "pH Calculator":
    h = st.number_input("[H+] concentration", min_value=0.0000000001, format="%.10f")

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