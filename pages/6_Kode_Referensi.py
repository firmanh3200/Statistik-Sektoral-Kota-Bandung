import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('KODE REFERENSI')

st.success('Kode Referensi Wilayah Kota Bandung')
@st.cache_data    
def kode_wilayah():
    # URL API Open Data
    url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_kelurahan?sort=id%3Aasc&page=1&per_page=10&where=%7B%22semester%22%3A%5B%221%22%5D%2C%22tahun%22%3A%5B%222024%22%5D%7D&where_or=%7B%7D"

    # Fungsi untuk mengambil data dari setiap halaman
    def fetch_data(url, page):
        response = requests.get(url, params={'page': page})
        data = response.json()
        return data

    # Mengambil semua data dengan memperhatikan pagination
    all_data = []
    page = 1
    while True:
        data = fetch_data(url, page)
        if 'data' in data:
            all_data.extend(data['data'])
            if data['pagination']['has_next']:
                page += 1
            else:
                break
        else:
            break
        
    # Menarik semua data
    data_penduduk = [item for item in all_data]

    # Mengubah data menjadi pandas dataframe
    df = pd.DataFrame(data_penduduk)
    
    df_kode = df[['kode_provinsi', 'nama_provinsi', 'bps_kode_kabupaten_kota', 'bps_nama_kabupaten_kota', 
                    'kemendagri_kode_kecamatan', 'kemendagri_nama_kecamatan', 'bps_kode_kecamatan',
                    'bps_nama_kecamatan', 'kemendagri_kode_desa_kelurahan', 'kemendagri_nama_desa_kelurahan', 
                    'bps_kode_desa_kelurahan', 'bps_desa_kelurahan']].astype(str)
    df_kode = df_kode.sort_values(by=['kemendagri_kode_kecamatan', 'kemendagri_kode_desa_kelurahan'])
    
    df_kode['Kode Dapodik Kemendikbud'] = ''
    df_kode['Kode EMIS Kemenag'] = ''
    
    st.dataframe(df_kode, hide_index=True, use_container_width=True)
    st.caption('Sumber: https://opendata.bandung.go.id/dataset')
            
if __name__ == '__main__':
    kode_wilayah()

st.divider()
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