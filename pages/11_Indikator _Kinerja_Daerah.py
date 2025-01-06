import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.subheader('Indikator Kinerja Daerah')
st.header('Kota Bandung 2024-2026', divider='rainbow')

st.success('Peraturan Wali Kota Bandung Nomor 14 Tahun 2023 tentang \
        Rencana Pembangunan Daerah Tahun 2024-2026')

data = pd.read_excel('data/indikator kinerja rkpd.xlsx')
data = data.dropna()
bidang = data['Bidang Urusan'].unique()

bidangterpilih = st.selectbox('Pilih Bidang/ Urusan', bidang)

if bidangterpilih:
    df = data[data['Bidang Urusan'] == bidangterpilih]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    #st.table(df)