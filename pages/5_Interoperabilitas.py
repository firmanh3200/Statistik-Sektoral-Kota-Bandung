import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')
st.subheader('Contoh Interoperabilitas Data', divider='green')

# URL gambar
url = "https://www.dragon1.com/images/dragon1-principle-interoperability.png"

# Mendapatkan gambar dari URL
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Menampilkan gambar di Streamlit
st.image(img, caption='Sumber: dragon1.com')

st.subheader('Apa itu Interoperabilitas?')
st.success('Interoperabilitas adalah kemampuan aplikasi dan sistem untuk secara aman \
    dan otomatis bertukar data tanpa memandang batas-batas geografis, politik, atau organisasi.')

st.warning('Berbagi data yang terkoordinasi di seluruh organisasi dan departemen sangat \
    penting di beberapa sektor untuk penelitian dan pengembangan serta pengalaman pengguna \
        akhir yang lebih baik.') 

st.info('Interoperabilitas mengacu pada standar, protokol, teknologi, dan mekanisme yang \
    memungkinkan data mengalir di antara sistem yang beragam dengan intervensi manusia yang minimal. \
    Hal ini memungkinkan beragam sistem untuk berkomunikasi satu sama lain dan berbagi informasi \
        secara waktu nyata. Solusi interoperabilitas mengurangi silo data dan membantu organisasi \
            mencapai komunikasi yang sesuai dengan industri. Ini berarti peningkatan efisiensi dan \
                penawaran layanan berkualitas lebih tinggi.')

st.divider()
st.write('@Forum Satu Data Kota Bandung')