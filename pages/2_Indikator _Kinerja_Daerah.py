import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout='wide')

st.subheader('Indikator Kinerja Daerah')
st.header('Kota Bandung 2024-2026', divider='rainbow')

with st.container(border=True):
    st.success('Peraturan Wali Kota Bandung Nomor 14 Tahun 2023 tentang \
            Rencana Pembangunan Daerah Tahun 2024-2026')

    data2 = pd.read_excel('data/indikator kinerja rkpd.xlsx')
    data2 = data2.dropna()
    bidang = data2['Bidang Urusan'].unique()

    bidangterpilih = st.selectbox('Pilih Bidang/ Urusan', bidang)

    if bidangterpilih:
        df2 = data2[data2['Bidang Urusan'] == bidangterpilih]
        
        st.dataframe(df2, use_container_width=True, hide_index=True)
    #st.table(df)

st.subheader('', divider='rainbow')
    
with st.container(border=True):
    st.info('Indikator Kinerja pada SIPD')
    url = 'https://sipd.go.id/ewalidata/a88eb731020c5bef7ecba8c2f445758c72371b56/?m=public_dssd_tabel&f=ajax_get_indikator&m=public_dssd_tabel&kodelokasi=3273&tahun_awal=2017&tahun_akhir=2025&draw=1&start=0&length=10000&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1736471306178'

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data['data'])
    
    indikator = df[['idindikator', 'kodeindikator', 'definisi_operasional', 'satuan', 'sumberdata', 'tipe_data', 'tag_urusan']]
    indikator['satuan'] = indikator['satuan'].str.split('<').str[0]
    tabel = indikator.dropna()
    
    st.dataframe(tabel, hide_index=True, use_container_width=True)
    st.caption('Sumber: https://sipd.go.id/ewalidata')
    
    urusan = tabel['tag_urusan'].unique()
    terpilih = st.selectbox('Filter Kode Urusan', urusan)
    
    if terpilih:
        tabel2 = tabel[tabel['tag_urusan'] == terpilih]
        st.dataframe(tabel2, hide_index=True, use_container_width=True)