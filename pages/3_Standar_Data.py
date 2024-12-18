import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

#st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('STANDAR DATA STATISTIK NASIONAL')
st.success('Berdasarkan Keputusan Kepala Badan Pusat Statistik Nomor 850 Tahun 2023')

# Fungsi untuk mendapatkan data dari API dengan paginasi
def get_all_data(base_url):
    all_data = []
    page = 0
    while True:
        url = f"{base_url}&page={page}"
        response = requests.get(url)
        data = response.json()
        if not data['content']:
            break
        all_data.extend(data['content'])
        page += 1
    return all_data

# URL dasar API
base_url = 'https://indah-api.bps.go.id/api/standar-data-statistik-nasional-2023?tipe=1&size=100'

# Mendapatkan semua data
all_data = get_all_data(base_url)

# Mengonversi data menjadi DataFrame
df = pd.DataFrame(all_data)
df = df.sort_values(by='namaData')

st.dataframe(df, hide_index=True, use_container_width=True)
st.caption('Sumber: https://indah.bps.go.id/standar-data-statistik-nasional')
st.divider()
st.write('@Forum Satu Data Kota Bandung')