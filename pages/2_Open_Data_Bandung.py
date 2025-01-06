import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

#st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('DAFTAR DATA DI OPEN DATA KOTA BANDUNG')

st.success('Kondisi Real Time Open Data Kota Bandung')

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
        
# URL yang diberikan
url2 = 'https://opendata.bandung.go.id/api/datasets?search=&sort=mdate%3Adesc&page=1&per_page=5000&where=%7B%22is_active%22%3Atrue%2C%22is_deleted%22%3Afalse%7D'

# Inisialisasi variabel untuk menyimpan semua data
all_data = []

# Mulai dari halaman pertama
page = 1

while True:
    # Membuat URL dengan parameter halaman
    url = f"{url2}&page={page}"
    
    # Mengambil data dari URL
    response = requests.get(url)
    data = response.json()
    
    # Memeriksa apakah ada data yang diambil
    if not data['data']:
        break
    
    # Menambahkan data ke dalam list all_data
    all_data.extend(data['data'])
    
    # Pindah ke halaman berikutnya
    page += 1

# Mengonversi data ke DataFrame pandas
df = pd.DataFrame(all_data)
df = df[df['organisasi_name'] != 'Badan Pusat Statistik Kota Bandung']
df = df[df['organisasi_name'] != 'Badan Meteorologi dan Geofisika']
df = df[df['organisasi_name'] != 'Kementrian Agama Kota Bandung']
df = df[df['organisasi_name'] != 'Otoritas Jasa Keuangan']
df = df[df['organisasi_name'] != 'Palang Merah Indonesia']
df = df[df['organisasi_name'] != 'Pengadilan Agama Bandung']
df = df[df['organisasi_name'] != 'Pengadilan Militer II-09 Bandung']
df = df[df['organisasi_name'] != 'Pengadilan Negeri Bandung']
df = df[df['organisasi_name'] != 'Pengadilan Tata Usaha Negara Bandung']
df = df[df['organisasi_name'] != 'Perusahaan Listrik Negara']

# Menampilkan semua baris data
pd.set_option('display.max_rows', None)

kolom_dipakai = ['organisasi_name', 'metadata', 'name']

df2 = df.copy()

# df2['organisasi_name'] != non_opd

st.subheader(f'Jumlah Data per Produsen Data di Kota Bandung')
kol1, kol2 = st.columns(2)
with kol1:
    # Menghitung jumlah kemunculan setiap organisasi_name
    df2_counts = df2['organisasi_name'].value_counts().reset_index()
    df2_counts.columns = ['organisasi_name', 'count']

    # Membuat chart
    fig = px.sunburst(df2_counts, path=['organisasi_name'], values='count')
    # Menambahkan nilai count ke dalam label
    fig.update_traces(textinfo='label+value')
    with st.container(border=True):
        st.plotly_chart(fig, use_container_width=True)
with kol2:
    with st.container(border=True):
        st.dataframe(df2_counts, use_container_width=True)
    
df2 = df[kolom_dipakai].sort_values(by='organisasi_name')

opd = df2['organisasi_name'].unique()

df2 = df2.rename(columns={'name':'Data yang Dihasilkan', 'organisasi_name':'Produsen Data'})

st.subheader("", divider='rainbow')
st.success('Statistik sektoral adalah statistik yang pemanfaatannya ditujukan untuk memenuhi \
            kebutuhan instansi tertentu dalam rangka penyelenggaraan tugas-tugas pemerintahan \
                dan pembangunan yang merupakan tugas pokok instansi yang bersangkutan.')

st.warning('Kamus Besar Bahasa Indonesia (KBBI) menjelaskan bahwa indikator \
merupakan sesuatu yang dapat memberikan petunjuk atau \
keterangan. Indikator juga bisa diartikan sebagai setiap ciri, \
karakteristik, atau ukuran yang bisa menunjukkan perubahan yang \
terjadi pada sebuah bidang tertentu.')

st.info('Suatu indikator biasanya diawali dengan kata Jumlah, Persentase, Proporsi, Rasio, \
    Rata-rata, Prevalensi, Indeks, Angka, atau Tingkat')

opd_terpilih = st.selectbox('Filter Produsen Data', opd)

# Ekstrak data yang diperlukan
extracted_data = []
for item in all_data:
    name = item["name"]
    dimensi_awal = next((meta["value"] for meta in item["metadata"] if meta["key"] == "Dimensi Dataset Awal"), None)
    dimensi_akhir = next((meta["value"] for meta in item["metadata"] if meta["key"] == "Dimensi Dataset Akhir"), None)
    organisasi_name = item["organisasi_name"]
    extracted_data.append({
        "name": name,
        "Dimensi Dataset Awal": dimensi_awal,
        "Dimensi Dataset Akhir": dimensi_akhir,
        "organisasi_name": organisasi_name
    })

# Buat DataFrame
df3 = pd.DataFrame(extracted_data)

if opd_terpilih:
    df3 = df3[df3['organisasi_name'] == opd_terpilih]
    df3 = df3.sort_values(by='name')
    df3 = df3.rename(columns={'name':'Output Data/ Indikator', 'Dimensi Dataset Awal':'data_awal',
                              'Dimensi Dataset Akhir':'data_akhir', 'organisasi_name':'Produsen Data'})
    
    st.dataframe(df3, use_container_width=True, hide_index=True)
    st.caption('Sumber: https://opendata.bandung.go.id/dataset')
    
    with st.expander(f'Daftar Metadata Statistik {opd_terpilih} Kota Bandung pada SIRUSA'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D={opd_terpilih}+Kota+Bandung" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D={opd_terpilih}+Kota+Bandung')
    
    with st.expander(f'Daftar Rekomendasi Terbit {opd_terpilih} Kota Bandung'):
        st.success(f'Rekomendasi {opd_terpilih} Kota Bandung')
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search={opd_terpilih}+Kota+Bandung" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search={opd_terpilih}+Kota+Bandung')

    st.subheader('', divider='green')    
    with st.expander(f'Contoh Metadata Statistik {opd_terpilih} di Pemerintah Daerah lain'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D={opd_terpilih}" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D={opd_terpilih}')

    with st.expander(f'Contoh Rancangan Kegiatan Statistik {opd_terpilih} di Pemerintah Daerah lain'):
        st.success(f'Contoh Rancangan Kegiatan {opd_terpilih} selindo')
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search={opd_terpilih}" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search={opd_terpilih}')

    
st.subheader("", divider='green')
with st.expander('BAHAN PEMBAHASAN FORUM SATU DATA UNTUK MENGIDENTIFIKASI KEGIATAN STATISTIK SEKTORAL:'):
    st.success('Data-data tersebut dihasilkan dari Bidang?')
    st.warning('Data-data tersebut dihasilkan dari kegiatan apa (Nama Kegiatan Statistik, jika produsen data mengalami kesulitan dalam menentukan, bisa merujuk ke Sirusa atau Romantik.)?')
    st.info('Apakah kegiatan tersebut sudah meminta Rekomendasi Pembina Data?')
    st.warning('Apakah sudah tersedia metadata (Kegiatan/MS-Keg, Indikator/MS-Ind, Variabel/MS-Var)?')
    st.info('Apakah data tersebut dikemas dalam sebuah laporan dan dianalisis?')
    st.success('Adakah data publik lain yang dihasilkan selain Daftar Data di atas?')
    st.warning('Data mana saja yang termasuk Data Prioritas Daerah?')
    st.info('Data mana saja yang akan dihasilkan kembali di tahun depan?')
    st.success('Apakah data-data tersebut sudah mengacu pada Standar Data Statistik Nasional?')
    st.info('Data mana saja yang sudah mengacu pada Data Induk Kementerian/ Lembaga Pengampu?')

st.divider()
st.write('@Forum Satu Data Kota Bandung')