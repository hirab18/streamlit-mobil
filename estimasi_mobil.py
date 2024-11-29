import pickle
import streamlit as st 

model = pickle.load(open('estimasi_mobil.sav', 'rb'))


st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

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
