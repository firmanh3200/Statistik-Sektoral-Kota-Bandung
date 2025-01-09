import streamlit as st
import pandas as pd

lke = pd.read_excel('data/lke-epss.xlsx', dtype={'KodeInd':'str'})
kematangan = pd.read_excel('data/kematangan.xlsx')

st.set_page_config(layout='wide')

st.subheader('Evaluasi Penyelenggaraan Statistik Sektoral', divider='rainbow')
st.warning('Sumber: https://drive.google.com/file/d/1B37k_35MENcx6MQ5UWmnV-EleC-derH0/view?usp=sharing')

with st.expander('PRINSIP SDI'):
        lke1 = lke[lke['Domain'] == 'Prinsip SDI']
        st.dataframe(lke1, hide_index=True, use_container_width=True)
        
        st.divider()
        kematangan1 = kematangan[kematangan['Kode'] == 1]
        indikator = kematangan1['Indikator'].unique()
        indterpilih = st.selectbox('Pilih Indikator', indikator)
        
        if indterpilih:
            kematangan1a = kematangan1[kematangan1['Indikator'] == indterpilih]
            st.table(kematangan1a)
        
        lke1a = lke1[lke1['Indikator'] == indterpilih]    
        penjelasan = lke1a['Penjelasan Indikator'].to_list()
        st.success('Penjelasan Indikator')
        st.write(penjelasan)
        
with st.expander('KUALITAS DATA'):
    lke2 = lke[lke['Domain'] == 'Kualitas Data']
    st.dataframe(lke2, hide_index=True, use_container_width=True)
    
    st.divider()
    kematangan2 = kematangan[kematangan['Kode'] == 2]
    indikator = kematangan2['Indikator'].unique()
    indterpilih = st.selectbox('Pilih Indikator', indikator)
    
    if indterpilih:
        kematangan2a = kematangan2[kematangan2['Indikator'] == indterpilih]
        st.table(kematangan2a)
        
    lke2a = lke2[lke2['Indikator'] == indterpilih]    
    penjelasan = lke2a['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)
    
with st.expander('PROSES BISNIS STATISTIK'):
    lke3 = lke[lke['Domain'] == 'Proses Bisnis Statistik']
    st.dataframe(lke3, hide_index=True, use_container_width=True)
    
    st.divider()
    kematangan3 = kematangan[kematangan['Kode'] == 3]
    indikator = kematangan3['Indikator'].unique()
    indterpilih = st.selectbox('Pilih Indikator', indikator)
    
    if indterpilih:
        kematangan3a = kematangan3[kematangan3['Indikator'] == indterpilih]
        st.table(kematangan3a)
        
    lke3a = lke3[lke3['Indikator'] == indterpilih]    
    penjelasan = lke3a['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)
    
with st.expander('KELEMBAGAAN'):
    lke4 = lke[lke['Domain'] == 'Kelembagaan']
    st.dataframe(lke4, hide_index=True, use_container_width=True)
    
    st.divider()
    kematangan4 = kematangan[kematangan['Kode'] == 4]
    indikator = kematangan4['Indikator'].unique()
    indterpilih = st.selectbox('Pilih Indikator', indikator)
    
    if indterpilih:
        kematangan4a = kematangan4[kematangan4['Indikator'] == indterpilih]
        st.table(kematangan4a)
        
    lke4a = lke4[lke4['Indikator'] == indterpilih]    
    penjelasan = lke4a['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)
    
with st.expander('STATISTIK NASIONAL'):
    lke5 = lke[lke['Domain'] == 'Statistik Nasional']
    st.dataframe(lke5, hide_index=True, use_container_width=True)
    
    st.divider()
    kematangan5 = kematangan[kematangan['Kode'] == 5]
    indikator = kematangan5['Indikator'].unique()
    indterpilih = st.selectbox('Pilih Indikator', indikator)
    
    if indterpilih:
        kematangan5a = kematangan5[kematangan5['Indikator'] == indterpilih]
        st.table(kematangan5a)
        
    lke5a = lke5[lke5['Indikator'] == indterpilih]    
    penjelasan = lke5a['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)

st.subheader('', divider='rainbow')

st.success('Kota Magelang meraih Predikat Terbaik 1 Nasional (Nilai IPS Tertinggi) Tahun 2024')
with st.expander('RANCANGAN KEGIATAN STATISTIK SEKTORAL KOTA MAGELANG'):
    iframe_code = f"""
    <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search=kota+magelang&instansi=0" width="100%" height="600" style="border:none;"></iframe>
    """

    st.markdown(iframe_code, unsafe_allow_html=True)
    st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search=kota+magelang&instansi=0')

with st.expander('METADATA STATISTIK SEKTORAL KOTA MAGELANG'):
    iframe_code = f"""
    <iframe src="https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D=kota+magelang" width="100%" height="600" style="border:none;"></iframe>
    """

    st.markdown(iframe_code, unsafe_allow_html=True)
    st.caption(f'Sumber: https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D=kota+magelang')

st.subheader('', divider='rainbow')

st.warning('Kota Malang meraih Predikat Terbaik 1 Nasional (Nilai IPS Tertinggi) Tahun 2023')
with st.expander('RANCANGAN KEGIATAN STATISTIK SEKTORAL KOTA MALANG'):
    iframe_code = f"""
    <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search=kota+malang&instansi=0" width="100%" height="600" style="border:none;"></iframe>
    """

    st.markdown(iframe_code, unsafe_allow_html=True)
    st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search=kota+malang&instansi=0')

with st.expander('METADATA STATISTIK SEKTORAL KOTA MALANG'):
    iframe_code = f"""
    <iframe src="https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D=kota+malang" width="100%" height="600" style="border:none;"></iframe>
    """

    st.markdown(iframe_code, unsafe_allow_html=True)
    st.caption(f'Sumber: https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D=kota+malang')

st.subheader('', divider='rainbow')

st.info('Kabupaten Sumedang meraih Predikat Terbaik Jawa Barat')
with st.expander('RANCANGAN KEGIATAN STATISTIK SEKTORAL KABUPATEN SUMEDANG'):
    iframe_code = f"""
    <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search=sumedang&instansi=0" width="100%" height="600" style="border:none;"></iframe>
    """

    st.markdown(iframe_code, unsafe_allow_html=True)
    st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search=sumedang&instansi=0')

with st.expander('METADATA STATISTIK SEKTORAL KABUPATEN SUMEDANG'):
    iframe_code = f"""
    <iframe src="https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D=sumedang" width="100%" height="600" style="border:none;"></iframe>
    """

    st.markdown(iframe_code, unsafe_allow_html=True)
    st.caption(f'Sumber: https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D=sumedang')


st.divider()
st.write('@Forum Satu Data Kota Bandung')

