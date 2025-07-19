import streamlit as st
import re

# ========== Konfigurasi Halaman ==========
st.set_page_config(page_title="Kalkulator Berat Molekul", page_icon="🧪", layout="centered")

# ========== Data Massa Atom Relatif (Ar) ==========
# Mengacu pada 2007 Atomic IUPAC oleh Wieser & Berglund
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

# ========== Header / Tampilan Depan ==========
st.image("assets/logo.png", width=120, caption="Program Studi Kimia Analitik", use_column_width=False)  # opsional
st.title("🧪 Kalkulator Berat Molekul Senyawa")
st.markdown("### Versi Ar: IUPAC 2007 – oleh Michael E. Wieser & Michael Berglund")

st.markdown("""
Aplikasi ini membantu menghitung berat molekul relatif (**Mr**) suatu senyawa kimia berdasarkan rumus kimia yang dimasukkan pengguna.

✅ **Cocok untuk:** Mahasiswa, dosen, analis laboratorium  
📗 **Referensi Ar:** Data resmi dari *IUPAC 2007*

> ✍️ **Contoh Input:**  
> `H2O`, `C6H12O6`, `NaCl`, `HNO3`  
> Untuk senyawa dengan tanda kurung seperti `Mg(OH)2`, tulis sebagai `MgO2H2`
""")

st.divider()

# ========== Fungsi Perhitungan Mr ==========
def hitung_mr(rumus):
    pola = r'([A-Z][a-z]?)(\d*)'
    hasil = re.findall(pola, rumus)
    total_mr = 0.0
    for unsur, jumlah in hasil:
        jumlah = int(jumlah) if jumlah else 1
        if unsur in ar_data:
            total_mr += ar_data[unsur] * jumlah
        else:
            st.error(f"Unsur '{unsur}' belum tersedia dalam data Ar kami.")
            return None
    return total_mr

# ========== Input Pengguna ==========
st.subheader("🔬 Masukkan Rumus Senyawa")
rumus = st.text_input("Contoh: H2O, NaCl, C6H12O6", value="H2O")

if st.button("Hitung Berat Molekul"):
    mr = hitung_mr(rumus)
    if mr:
        st.success(f"💡 Berat molekul (Mr) dari **{rumus}** adalah **{mr:.2f} g/mol**")

# ========== Footer ==========
st.markdown("---")
st.markdown("📘 *© 2025 Kalkulator Berat Molekul – Kelompok 6 Kimia Analitik*")
