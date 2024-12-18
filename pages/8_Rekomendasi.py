import streamlit as st

st.set_page_config(layout='wide')

st.header('Rekomendasi Kegiatan Statistik Sektoral', divider='rainbow')

with st.expander('Dasar Hukum'):
    st.warning('Peraturan BPS No. 4 Tahun 2019 tentang NSPK Penyelenggaraan Statistik \
        Sektoral oleh Pemerintah Daerah')

st.subheader('Pasal 12')
st.success('1. Pemerintah Daerah penyelenggara kegiatan Statistik Sektoral yang hasilnya dipublikasikan, \
            wajib menyerahkan hasilnya kepada BPS.')

st.info('2. Hasil penyelenggaraan kegiatan Statistik Sektoral yang dimaksud dalam bentuk softcopy.')

st.warning('3. Hasil penyelenggaraan diserahkan melalui Walidata.')

st.subheader('', divider='rainbow')

st.link_button('Ajukan Permohonan Rekomendasi', 'https://romantik.web.bps.go.id/')

st.link_button('Daftar Rekomendasi', 'https://romantik.bps.go.id/site/pencarian/')

st.divider()
st.write('@Forum Satu Data Kota Bandung')