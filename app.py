import streamlit as st
import re

# Data massa atom relatif (Ar)
ar_data = {
    "H": 1.008, "C": 12.01, "O": 16.00, "N": 14.01, "Cl": 35.45,
    "Na": 22.99, "S": 32.06, "K": 39.10, "Mg": 24.31, "Ca": 40.08,
    "Fe": 55.85, "P": 30.97, "Zn": 65.38
}

st.set_page_config(page_title="Kalkulator Berat Molekul", page_icon="🧪")

st.title("🧪 Kalkulator Berat Molekul Senyawa")
st.markdown("Masukkan rumus senyawa (misal: `H2O`, `C6H12O6`, `NaCl`) lalu klik hitung.")

# Fungsi hitung berat molekul
def hitung_mr(rumus):
    pola = r'([A-Z][a-z]?)(\d*)'
    hasil = re.findall(pola, rumus)

    total_mr = 0.0
    for unsur, jumlah in hasil:
        jumlah = int(jumlah) if jumlah else 1
        if unsur in ar_data:
            total_mr += ar_data[unsur] * jumlah
        else:
            st.error(f"Unsur '{unsur}' belum tersedia dalam data Ar.")
            return None
    return total_mr

# Input
rumus = st.text_input("Rumus Senyawa:", value="H2O")

# Output
if st.button("Hitung"):
    mr = hitung_mr(rumus)
    if mr:
        st.success(f"Berat molekul (Mr) dari **{rumus}** adalah **{mr:.2f} g/mol**")

st.caption("© 2025 Kalkulator Mr - Kimia Analitik")
