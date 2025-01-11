import streamlit as st
import pandas as pd
import requests

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

with st.expander(f'Daftar Rekomendasi Terbit Kota Bandung:'):
    tahun = ['2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028']
    
    tahun2 = st.selectbox('Filter Tahun Terbit', tahun)
    
    if tahun2:
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search=kota+bandung&tahun={tahun2}&provinsi=0&kabkot=0&instansi=0" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search=kota+bandung&tahun={tahun2}&provinsi=0&kabkot=0&instansi=0')

st.subheader('', divider='rainbow')

with st.expander(f'Contoh Permintaan Rekomendasi (Rancangan Kegiatan Statistik Sektoral):'):
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
        
    df = df.sort_values(by='organisasi_name')
    opd = df['organisasi_name'].unique()
    
    opdterpilih = st.selectbox('Filter OPD', opd)
    
    if opdterpilih:
        st.success(f'Contoh Rancangan Kegiatan {opdterpilih} selindo')
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search={opdterpilih}" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search={opdterpilih}')

st.subheader('', divider='rainbow')

with st.expander('CONTOH REKOMENDASI ROMANTIK'):
    st.success('Kompilasi Data Untuk Pengukuran Indikator Kinerja Pelaksanaan Anggaran (IKPA) Kementerian Negara/Lembaga Tahun 2025, \
            Kementerian Keuangan, https://romantik.web.bps.go.id/rekomendasi-terbit/aDJ5Y2hGSGFUeVdrbGY0N1NFcEdFQT09')
    
with st.expander('CONTOH REKOMENDASI SURVEI'):
    st.success('Survei Kesiapan Kementerian Hukum dan Ham dalam Proses Penyederhanaan dan Transformasi Jabatan Administrasi ke Jabatan Fungsional, \
            Badan Penelitian dan Pengembangan Hukum dan Ham, \
                https://romantik.bps.go.id/site/getmodalpencarian/?tipe=survei&pelabelan=Survei+Kesiapan+Kementerian+Hukum+dan+Ham+dalam+Proses+Penyederhanaan+dan+Transformasi+Jabatan+Administrasi+ke+Jabatan+Fungsional&kode=640&nama=Survei+Kesiapan+Kementerian+Hukum+dan+Ham+dalam+Proses+Penyederhanaan+dan+Transformasi+Jabatan+Administrasi+ke+Jabatan+Fungsional&_=1736561322189')

st.subheader('', divider='rainbow')

st.link_button('Cari Contoh Rancangan Kegiatan Lainnya', 'https://romantik.web.bps.go.id/rekomendasi-terbit')
st.link_button('Ajukan Permohonan Rekomendasi', 'https://romantik.web.bps.go.id/')

st.divider()
st.write('@Forum Satu Data Kota Bandung')