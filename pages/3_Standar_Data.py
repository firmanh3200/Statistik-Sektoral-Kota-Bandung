import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

#st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('STANDAR DATA STATISTIK NASIONAL')
st.success('Berdasarkan Keputusan Kepala Badan Pusat Statistik Nomor 850 Tahun 2023')

# Fungsi untuk mendapatkan data dari API dengan paginasi
st.warning('Standar Data Statistik Nasional')
# Embed URL in an iframe
iframe_code = f"""
<iframe src="https://indah.bps.go.id/standar-data-statistik-nasional" width="100%" height="600" style="border:none;"></iframe>
"""

st.markdown(iframe_code, unsafe_allow_html=True)

st.caption('Sumber: https://indah.bps.go.id/standar-data-statistik-nasional')
st.divider()
st.write('@Forum Satu Data Kota Bandung')