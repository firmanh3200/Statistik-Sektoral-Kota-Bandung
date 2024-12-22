import streamlit as st
import pandas as pd

lke = pd.read_excel('data/lke-epss.xlsx', dtype={'KodeInd':'str'})
kematangan = pd.read_excel('data/kematangan.xlsx')

st.set_page_config(layout='wide')

st.subheader('Evaluasi Penyelenggaraan Statistik Sektoral', divider='rainbow')
st.warning('Sumber: https://drive.google.com/file/d/1B37k_35MENcx6MQ5UWmnV-EleC-derH0/view?usp=sharing')

with st.expander('TINGKAT KEMATANGAN'):
    st.success(':red[RINTISAN]:  penyelenggaraan statistik sektoral dilakukan \
                :red[tanpa perencanaan dan sewaktu-waktu]')
    
    st.info(':red[TERKELOLA]: penyelenggaraan statistik sektoral sudah \
            dilakukan sesuai dengan fungsi manajemen dan \
            diterapkan pada :red[sebagian unit kerja] dalam organisasi')
    
    st.warning(':red[TERDEFINISI]: penyelenggaraan statistik sektoral sudah \
            dilakukan sesuai dengan fungsi manajemen yang \
            sesuai pedoman/standar dan diterapkan pada \
            semua unit kerja dalam organisasi')
    
    st.success(':red[TERPADU DAN TERUKUR]: penyelenggaraan statistik sektoral telah \
            dilakukan secara terpadu dan telah berkontribusi \
            pada kinerja organisasi. Kinerja Penyelenggaraan \
            Statistik Sektoral dapat diukur melalui kegiatan \
            :red[reviu dan evaluasi pada setiap proses]')
    
    st.info(':red[OPTIMUM]: penyelenggaraan statistik sektoral telah \
            dilakukan :red[peningkatan kualitas secara \
            berkesinambungan] berdasarkan hasil reviu dan \
            evaluasi')
    
with st.expander('PRINSIP SDI'):
    # st.success('Tingkat Kematangan Penerapan Standar Data Statistik (SDS)')
    # st.info('Tingkat Kematangan Penerapan Metadata Statistik')
    # st.warning('Tingkat Kematangan Penerapan Interoperabilitas Data')
    # st.info('Tingkat Kematangan Penerapan Kode Referensi dan/atau Data Induk')
    lke1 = lke[lke['Domain'] == 'Prinsip SDI']
    st.dataframe(lke1, hide_index=True, use_container_width=True)
    st.divider()
    kematangan1 = kematangan[kematangan['Kode'] == 1]
    st.dataframe(kematangan1, hide_index=True, use_container_width=True)
    penjelasan = lke1['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)
    
with st.expander('KUALITAS DATA'):
    # st.success('Tingkat Kematangan Relevansi Data Terhadap Pengguna')
    # st.info('Tingkat Kematangan Proses Identifikasi Kebutuhan Data')
    # st.warning('Tingkat Kematangan Penilaian Akurasi Data')
    # st.info('Tingkat Kematangan Penjaminan Aktualitas Data')
    # st.success('Tingkat Kematangan Pemantauan Ketepatan Waktu Diseminasi')
    # st.info('Tingkat Kematangan Ketersediaan Data untuk Pengguna Data')
    # st.warning('Tingkat Kematangan Akses Media Penyebarluasan Data')
    # st.info('Tingkat Kematangan Penyediaan Format Data')
    # st.success('Tingkat Kematangan Keterbandingan Data')
    # st.info('Tingkat Kematangan Konsistensi Statistik')
    lke2 = lke[lke['Domain'] == 'Kualitas Data']
    st.dataframe(lke2, hide_index=True, use_container_width=True)
    st.divider()
    kematangan2 = kematangan[kematangan['Kode'] == 2]
    st.dataframe(kematangan2, hide_index=True, use_container_width=True)
    penjelasan = lke2['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)
    
with st.expander('PROSES BISNIS STATISTIK'):
    # st.success('Tingkat Kematangan Pendefinisian Kebutuhan Statistik')
    # st.info('Tingkat Kematangan Desain Statistik')
    # st.warning('Tingkat Kematangan Penyiapan Instrumen')
    # st.info('Tingkat Kematangan Proses Pengumpulan Data / Akuisisi Data Statistik')
    # st.success('Tingkat Kematangan Pengolahan Data Statistik')
    # st.info('Tingkat Kematangan Analisis Data Statistik')
    # st.warning('Tingkat Kematangan Diseminasi Data Statistik')
    lke3 = lke[lke['Domain'] == 'Proses Bisnis Statistik']
    st.dataframe(lke3, hide_index=True, use_container_width=True)
    st.divider()
    kematangan3 = kematangan[kematangan['Kode'] == 3]
    st.dataframe(kematangan1, hide_index=True, use_container_width=True)
    penjelasan = lke3['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)
    
with st.expander('KELEMBAGAAN'):
    # st.success('Tingkat Kematangan Penjaminan Transparansi Informasi Statistik')
    # st.info('Tingkat Kematangan Penjaminan Netralitas dan Obyektivitas \
    #         terhadap penggunaan Sumber Data Metodologi')
    # st.warning('Tingkat Kematangan Penjaminan Kualitas Data Statistik')
    # st.info('Tingkat Kematangan Penjaminan Konfidensialitas Data Statistik')
    # st.success('Tingkat Kematangan Penerapan Kompetensi Sumber Daya Manusia Bidang Statistik')
    # st.info('Tingkat Kematangan Penerapan Kompetensi Sumber Daya Manusia Bidang Manajemen Data Statistik')
    # st.warning('Tingkat Kematangan Kolaborasi Penyelenggaraan Kegiatan Statistik')
    # st.info('Tingkat Kematangan Penyelenggaraan Forum Satu Data')
    # st.success('Tingkat Kematangan Kolaborasi dengan Pembina Data Statistik')
    # st.info('Tingkat Kematangan Penyelenggaraan Pelaksanaan Tugas Sebagai Wali Data')
    lke4 = lke[lke['Domain'] == 'Kelembagaan']
    st.dataframe(lke4, hide_index=True, use_container_width=True)
    st.divider()
    kematangan4 = kematangan[kematangan['Kode'] == 4]
    st.dataframe(kematangan4, hide_index=True, use_container_width=True)
    penjelasan = lke4['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)
    
with st.expander('STATISTIK NASIONAL'):
    # st.success('Tingkat Kematangan Penggunaan Data Statistik Dasar untuk \
    #         Perencanaan, Monitoring, dan Evaluasi, dan atau Penyusunan Kebijakan')
    # st.info('Tingkat Kematangan Penggunaan Data Statistik Sektoral untuk \
    #         Perencanaan, Monitoring, dan Evaluasi, dan atau Penyusunan Kebijakan')
    # st.warning('Tingkat Kematangan Sosialisasi dan Literasi Hasil Statistik')
    # st.info('Tingkat Kematangan Kepatuhan Penerapan Rekomendasi Kegiatan Statistik')
    # st.success('Tingkat Kematangan Perencanaan Pembangunan Statistik')
    # st.info('Tingkat Kematangan Penyebarluasan Data Statistik')
    # st.warning('Tingkat Kematangan Pemanfaatan Big Data untuk Mendukung Statistik')
    lke5 = lke[lke['Domain'] == 'Statistik Nasional']
    st.dataframe(lke5, hide_index=True, use_container_width=True)
    st.divider()
    kematangan5 = kematangan[kematangan['Kode'] == 5]
    st.dataframe(kematangan5, hide_index=True, use_container_width=True)
    penjelasan = lke5['Penjelasan Indikator'].to_list()
    st.success('Penjelasan Indikator')
    st.write(penjelasan)