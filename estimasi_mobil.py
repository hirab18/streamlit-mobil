import os
import pickle
import streamlit as st

# Menentukan lokasi file model
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'estimasi_mobil.sav')

# Memuat model dari file
with open(file_path, 'rb') as file:
    model = pickle.load(file)

st.title('Estimasi Harga Mobil Bekas')

# Input pengguna
year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

# Estimasi harga mobil ketika tombol ditekan
if st.button('Estimasi Harga'):
    # Melakukan prediksi harga
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    
    # Mengakses nilai pertama dari prediksi (karena predict mengembalikan array)
    estimated_price = predict[0]
    
    # Menampilkan hasil estimasi harga dalam Pounds
    st.write('Estimasi harga Mobil bekas dalam Ponds: ', estimated_price)
    
    # Mengonversi harga ke IDR (dalam juta)
    estimated_price_idr = estimated_price * 19000
    st.write('Estimasi harga mobil bekas dalam IDR (Juta):', estimated_price_idr)
