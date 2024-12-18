import streamlit as st

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

st.subheader('Materi Pembinaan Statistik Sektoral', divider='green')

with st.expander('PROSES BISNIS STATISTIK'):
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.link_button("Dasar-dasar Statistik", url="https://drive.google.com/file/d/1cmB7U6qWBQYrG_5sUiuKJyz4EDb20IL5/preview")

        st.link_button("Perencanaan Kegiatan", url="https://drive.google.com/file/d/1Ocu8Kwz10WeQeRaS2FaAdLlKCGrWaQKo/preview")

        st.link_button("Perancangan Kegiatan", url="https://drive.google.com/file/d/1XT98Jg_G1jbAT3yNeTz1gTvQkMrjUwZA/preview")

    with kolom2:
        st.link_button("Pengumpulan Data", url="https://drive.google.com/file/d/1EqRNPp19xhPI7Njc_yEii2QQvBV2WPb1/preview")

        st.link_button("Pengolahan Data", url="https://drive.google.com/file/d/18TFFNbZaDUt9JJkMalDhlynYP4--7ZlE/preview")

        st.link_button("Analisis Statistik", url="https://drive.google.com/file/d/1Gakcm7etk2V-YQ-PFkC51Rbf3oO1kvXN/preview")

    with kolom3:
        st.link_button("Diseminasi dan Evaluasi", url="https://drive.google.com/file/d/1WLuE8fo5vu3QADpTPuYKJQUTQdY6Xs6P/preview")
        
        st.link_button("Aplikasi Kegiatan Statistik", url="https://drive.google.com/file/d/18Em1hySNdkAoEt4YJysUblFd0eQGOIwX/preview")
        
        st.link_button("Metadata Statistik", url="https://drive.google.com/file/d/1fngDi4qmpwTMlX83AkqUk9PydQguFq-W/preview")
        

with st.expander('PENYELENGGARAAN STATISTIK SEKTORAL'):
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.link_button("Satu Data Indonesia", url="https://drive.google.com/file/d/1STnvC6GOmaImybDi5PdJwStine-kTXw2/view?usp=sharing")

        st.link_button("Kualitas Data", url="https://drive.google.com/file/d/1MXduD16UdSjHK9zCU_GloQ1bnSaawi4u/view?usp=sharing")

        st.link_button("Proses Bisnis Statistik", url="https://drive.google.com/file/d/1rGRIdKws-JnF8qW4mlw60NYljeqzq1of/view?usp=sharing")

    with kolom2:
        st.link_button("Kelembagaan", url="https://drive.google.com/file/d/1e8eTnj2jA968pUJy1_cNyh9cKSMoCJDk/view?usp=sharing")

        st.link_button("Sistem Statistik Nasional", url="https://drive.google.com/file/d/1AMdjtkt4rkze9oW3zyi0pKouEy2291kM/view?usp=sharing")

        st.link_button("Standar Data", url="https://drive.google.com/file/d/1Q6CNMjJAiQlPS-aqcf4_PkyDp2KsxtU0/view?usp=sharing")

    with kolom3:
        st.link_button("Rekomendasi Survei", url="https://drive.google.com/file/d/1aY9eLyVRtZ84lOcl1fjVaCrqohCI6L7Z/view?usp=sharing")
        
        st.link_button("Big Data", url="https://drive.google.com/file/d/1jb7YOLwRHlWvXAYoZF5q60oMaOtYZ_70/view?usp=sharing")
        
        st.link_button("Manajemen Kualitas", url="https://drive.google.com/file/d/1w6YVhX4ZnjzuiKy6GVHEpHG0cmWPLaPe/view?usp=sharing")
        
st.divider()
st.write('@Forum Satu Data Kota Bandung')