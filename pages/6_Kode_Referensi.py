import streamlit as st

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('KODE REFERENSI')

# Daftar opsi dan URL yang sesuai
pilihan = {
    "Kesehatan": "https://data.go.id/list-data-kode-referensi-info/2",
    "Perlindungan Sosial": "https://data.go.id/list-data-kode-referensi-info/3",
    "Ekonomi": "https://data.go.id/list-data-kode-referensi-info/4",
    "Lingkungan": "https://data.go.id/list-data-kode-referensi-info/7",
    "Budaya": "https://data.go.id/list-data-kode-referensi-info/9",
    "Agama": "https://data.go.id/list-data-kode-referensi-info/10",
    "Wilayah Administrasi Pemerintahan dan Pulau": "https://data.go.id/list-data-kode-referensi-info/1",
    "Industri": "https://data.go.id/list-data-kode-referensi-info/5",
    "KBLI": "https://data.go.id/list-data-kode-referensi-info/6",
    "Sumber Daya Alam": "https://data.go.id/list-data-kode-referensi-info/8",
    "Pembangunan Daerah": "https://data.go.id/list-data-kode-referensi-info/11",
    "Pendidikan": "https://data.go.id/list-data-kode-referensi-info/12",
    "Ketenagakerjaan": "https://data.go.id/list-data-kode-referensi-info/13",
    "Pemerintahan Umum": "https://data.go.id/list-data-kode-referensi-info/14",
    "Pertahanan": "https://data.go.id/list-data-kode-referensi-info/15",
    "Luar Negeri": "https://data.go.id/list-data-kode-referensi-info/16",
}

# Membuat dropdown
selected_option = st.selectbox("Pilih Kategori:", list(pilihan.keys()))

# Tombol untuk membuka URL di tab baru
if st.button("Buka Tautan"):
    url = pilihan[selected_option]
    st.markdown(f'<a href="{url}" target="_blank">Klik di sini untuk membuka Kode Referensi Kategori {selected_option}</a>', unsafe_allow_html=True)

st.warning('Baca Pedoman: https://drive.google.com/file/d/1B37k_35MENcx6MQ5UWmnV-EleC-derH0/view?usp=sharing')

st.divider()
st.write('@Forum Satu Data Kota Bandung')