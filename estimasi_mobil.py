import os
import pickle
import streamlit as st
import numpy as np  # Untuk validasi input numerik

# Mendapatkan path file estimasi_mobil.sav
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'estimasi_mobil.sav')

# Memastikan file estimasi_mobil.sav tersedia
if not os.path.exists(file_path):
    st.error(f"File 'estimasi_mobil.sav' tidak ditemukan di lokasi: {file_path}")
    st.stop()

# Memuat model menggunakan pickle
try:
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Gagal memuat model. Error: {e}")
    st.stop()

# Judul aplikasi
st.title('Estimasi Harga Mobil Bekas')

# Input dari pengguna
year = st.number_input('Input Tahun Mobil', min_value=1900, max_value=2025, step=1, value=2020)
mileage = st.number_input('Input Km Mobil', min_value=0.0, step=100.0, value=10000.0)
tax = st.number_input('Input Pajak Mobil', min_value=0.0, step=10.0, value=200.0)
mpg = st.number_input('Input Konsumsi BBM Mobil (MPG)', min_value=0.0, step=1.0, value=30.0)
engineSize = st.number_input('Input Engine Size (Liter)', min_value=0.0, step=0.1, value=1.5)

# Tombol untuk melakukan prediksi
if st.button('Estimasi Harga'):
    try:
        # Validasi input sebelum prediksi
        if any(value <= 0 for value in [year, mileage, tax, mpg, engineSize]):
            st.error("Semua input harus bernilai lebih dari 0.")
        else:
            # Melakukan prediksi
            prediction = model.predict([[year, mileage, tax, mpg, engineSize]])
            price_in_pounds = prediction[0]
            price_in_idr = price_in_pounds * 19000  # Konversi ke Rupiah

            # Menampilkan hasil
            st.write(f"Estimasi harga mobil bekas dalam Pounds: £{price_in_pounds:,.2f}")
            st.write(f"Estimasi harga mobil bekas dalam IDR (Juta): Rp{price_in_idr / 1_000_000:,.2f} juta")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi. Error: {e}")
