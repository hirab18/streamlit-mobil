import os
import pickle
import streamlit as st 

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'estimasi_mobil.sav')
model = pickle.load(open('models/estimasi_mobil.sav', 'rb'))


st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga Mobil bekas dalam Ponds : ', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta) :', predict*19000)
