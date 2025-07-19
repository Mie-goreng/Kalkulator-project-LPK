import streamlit as st
import re

# Konfigurasi halaman
st.set_page_config(page_title="Chem‑Calc Mr", page_icon="⚛️", layout="wide")

# Palet warna ala Valorant
primary = "#f91017"
bg = "#080609"
text = "#ECE6E8"

# CSS custom style
st.markdown(f"""
<style>
body {{background-color: {bg}; color: {text};}}
.stButton>button {{background-color: {primary}; color: white; border-radius: 8px; padding: 0.5em 1.5em;}}
.stTextInput>div>input {{background-color: #1a1a1a; color: {text}; border: none; padding: 0.5em; border-radius: 4px;}}
h1 {{color: {primary};}}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# ⚛️ Kalkulator Berat Molekul")
st.markdown("### Hitung Mr senyawa kimia dengan gaya high‑contrast Valorant")

st.markdown("Masukkan rumus senyawa, contoh: `H2O`, `C6H12O6`, `NaCl`.\nUntuk `Mg(OH)2`, gunakan `MgO2H2`.")

st.divider()

# Data Ar
ar_data = {
    "H": 1, "C": 12, "O": 16, "N": 14, "Cl": 35.45, "Br": 79.904, "B": 10.811,
    "Cr": 51.996, "Co": 58.933, "Cu": 63.546, "F": 18.998, "He": 4.002, "I": 126.904,
    "La": 138.905, "Pb": 207.2, "Li": 6.94, "Na": 22.99, "S": 32.06, "K": 39.10,
    "Mg": 24.31, "Ca": 40.08, "Fe": 55.85, "P": 30.97, "Zn": 65.38, "Al": 26.98,
    "Ar": 39.948, "Ba": 137.327, "Mn": 54.938, "Hg": 200.59, "Ne": 20.179,
    "Ni": 58.693, "Ag": 107.868, "Be": 9.012, "Rb": 85.4678, "Sc": 44.955,
    "Si": 28.085, "Xe": 131.293, "Pt": 195.084, "Ga": 69.723, "Ge": 72.64,
    "As": 74.921, "Kr": 83.798, "Sr": 87.62, "Pd": 106.42, "Cd": 112.411,
    "Cs": 132.905, "Ce": 140.116, "Bi": 208.980, "Ir": 192.217
}

# Kalkulasi Mr
def hitung_mr(rumus):
    matches = re.findall(r'([A-Z][a-z]?)(\d*)', rumus)
    total = 0.0
    for atom, jumlah in matches:
        jumlah = int(jumlah) if jumlah else 1
        if atom in ar_data:
            total += ar_data[atom] * jumlah
        else:
            st.error(f"Unsur '{atom}' tidak tersedia.")
            return None
    return total

# Input dan tombol
rumus = st.text_input("", value="H2O")
if st.button("Hitung"):
    mr = hitung_mr(rumus)
    if mr is not None:
        st.markdown(f"### Mr dari **{rumus}** = **{mr:.2f} g/mol**")

st.divider()
st.markdown(f"<div style='text-align:center;color:{text}'>© 2025 Chem‑Calc | Streamlit | IUPAC 2007</div>", unsafe_allow_html=True)
