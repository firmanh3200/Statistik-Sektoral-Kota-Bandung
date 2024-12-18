import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

#st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('DAFTAR DATA STATISTIK SEKTORAL KOTA BANDUNG DI OPEN DATA JABAR')

wilayah = 'Kota Bandung'

st.success('Kondisi Real Time Open Data Jabar')

# wilayah_terpilih = st.selectbox("Pemerintah Kabupaten:", wilayah)

custom_css = """
<style>
    .dataframe td {
        white-space: pre-wrap;
    }
</style>
"""

# Menyisipkan CSS khusus
st.markdown(custom_css, unsafe_allow_html=True)
        
# 3207
if wilayah:
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=12"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df.copy()
    non_opd = ['Otoritas Jasa Keuangan', 'Palang Merah Indonesia', 'Kementrian Agama Kota Bandung',
               'Perusahaan Listrik Negara', 'Pengadilan Agama Bandung', 'Pengadilan Negeri Bandung',
               'Pengadilan Tata Usaha Negara Bandung', 'Pengadilan Militer II-09 Bandung',
               'Badan Meteorologi dan Geofisika', 'Perusahaan Daerah Air Minum Tirtawening']
    
    # df2['nama_skpd'] != non_opd
    
    st.subheader(f'Jumlah Data per Produsen Data di {wilayah}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
       
st.subheader("", divider='green')
with st.expander('BAHAN PEMBAHASAN FORUM SATU DATA UNTUK MENGIDENTIFIKASI KEGIATAN STATISTIK SEKTORAL:'):
    st.success('Data-data tersebut dihasilkan dari Bidang?')
    st.warning('Data-data tersebut dihasilkan dari kegiatan apa (Nama Kegiatan Statistik, jika produsen data mengalami kesulitan dalam menentukan, bisa merujuk ke Sirusa atau Romantik.)?')
    st.info('Apakah kegiatan tersebut sudah meminta Rekomendasi Pembina Data?')
    st.success('Adakah data publik lain yang dihasilkan selain Daftar Data di atas?')
    st.warning('Data mana saja yang termasuk Data Prioritas Daerah?')
    st.info('Data mana saja yang akan dihasilkan kembali di tahun depan?')
    st.success('Apakah data-data tersebut sudah mengacu pada Standar Data Statistik Nasional?')
    st.warning('Apakah sudah tersedia metadata (Kegiatan/MS-Keg, Indikator/MS-Ind, Variabel/MS-Var)?')
    st.info('Data mana saja yang sudah mengacu pada Data Induk Kementerian/ Lembaga Pengampu?')

st.divider()
st.write('@Forum Satu Data Kota Bandung')