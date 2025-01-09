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

st.subheader('', divider=True)

with st.container(border=True):
    st.subheader('Implementasi Kode Referensi')
    
    # PPATK
    with st.expander('PPATK'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://satudata.ppatk.go.id/pages/kode-referensi-dan-data-induk" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://satudata.ppatk.go.id/pages/kode-referensi-dan-data-induk')

    # Kemenkes
    with st.expander('Kementerian Kesehatan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://opendata.karanganyarkab.go.id/dataset/7ccf725f-0461-4ca4-84aa-80c0c0b1dc4b/resource/729c486c-ca16-4b14-8170-330b2349887c/download/2022-kepmenkes-nomor-hk.01.07_menkes_223_2022.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://opendata.karanganyarkab.go.id/dataset/7ccf725f-0461-4ca4-84aa-80c0c0b1dc4b/resource/729c486c-ca16-4b14-8170-330b2349887c/download/2022-kepmenkes-nomor-hk.01.07_menkes_223_2022.pdf')

    # Kemendikbudristek
    with st.expander('Kemendikbudristek'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://referensi.data.kemdikbud.go.id/" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://referensi.data.kemdikbud.go.id/')

    # Kementerian Keuangan
    with st.expander('Kementerian Keuangan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://www.satudja.kemenkeu.go.id/pandu/modul/referensi/" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://www.satudja.kemenkeu.go.id/pandu/modul/referensi/')

    # Klasifikasi Statistik
    with st.expander('Klasifikasi Statistik'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://sibaku.bps.go.id/sibaku/tentangkls" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://sibaku.bps.go.id/sibaku/tentangkls')

    # Kemaritiman
    with st.expander('Kemaritiman dan Investasi'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://jdih.maritim.go.id/kamushukum/kode-referensi" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://jdih.maritim.go.id/kamushukum/kode-referensi')

    # BIG
    with st.expander('Badan Informasi Geospasial'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://katalog.data.go.id/dataset/administrasi_ar_desakel2" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://katalog.data.go.id/dataset/administrasi_ar_desakel2')

    # Perencanaan Pembangunan
    with st.expander('Kodefikasi Perencanaan Pembangunan Daerah'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://api-e-database.kemendagri.go.id/uploads/foto/1719908195420.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://api-e-database.kemendagri.go.id/uploads/foto/1719908195420.pdf')

    # Kode Wilayah Kemendagri
    with st.expander('Kode Wilayah Administrasi Pemerintahan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://api-e-database.kemendagri.go.id/uploads/foto/1715587369092.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://api-e-database.kemendagri.go.id/uploads/foto/1715587369092.pdf')

    # Perhubungan
    with st.expander('Kementerian Perhubungan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://portaldata.kemenhub.go.id/kode-referensi" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://portaldata.kemenhub.go.id/kode-referensi')
    
    # ISBN
    with st.expander('International Standard Book Number'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://isbn.perpusnas.go.id/landing_page/home" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://isbn.perpusnas.go.id/landing_page/home')
    
    # Kode Pemda MenPAN
    with st.expander('Kode Pemda MenPAN'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://eskld-v2.menpan.go.id/pemerintah-daerah/provinsi/13" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://eskld-v2.menpan.go.id/pemerintah-daerah/provinsi/13')
    
    # Arsitektur SPBE
    with st.expander('Arsitektur SPBE'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://jdih.setkab.go.id/PUUdoc/176876/Salinan_Perpres_Nomor_132_Tahun_2022.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://jdih.setkab.go.id/PUUdoc/176876/Salinan_Perpres_Nomor_132_Tahun_2022.pdf')
    
    # Kelautan Perikanan
    with st.expander('Kelautan dan Perikanan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://jdih.kkp.go.id/bahanrapat/bahanrapat_24052021044725.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://jdih.kkp.go.id/bahanrapat/bahanrapat_24052021044725.pdf')
    
    # Kode HS
    with st.expander('Harmonized System'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://www.insw.go.id/intr" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://www.insw.go.id/intr')
    
    # Ekspor Impor
    with st.expander('Efisiensi Proses Ekpsor Impor'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://www.insw.go.id/intr/referensi" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://www.insw.go.id/intr/referensi')
    
    # Data Induk Pendidikan
    with st.expander('Data Induk Kemendikbudristek'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://data.kemdikbud.go.id/data-induk" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://data.kemdikbud.go.id/data-induk')
    
    # Data Induk Ikan
    with st.expander('Data Induk Ikan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://jdih.kkp.go.id/Homedev/DetailPeraturan/3029" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://jdih.kkp.go.id/Homedev/DetailPeraturan/3029')
    
    # ISIC
    with st.expander('International Standard Industrial Classification of All Economic Activities'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://unstats.un.org/unsd/publication/seriesm/seriesm_4rev4e.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://unstats.un.org/unsd/publication/seriesm/seriesm_4rev4e.pdf')
    
    # ISO
    with st.expander('International Organization of Standardizations'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://www.iso.org/popular-standards.html" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://www.iso.org/popular-standards.html')
    
    # Kode Pos
    # URL dasar dengan placeholder untuk nomor halaman
    url_head = 'https://kodepos.co.id/kodepos/jawa-barat?page={}'

    # Buat list untuk menyimpan DataFrame dari setiap halaman
    dataframes = []

    # Iterasi melalui setiap halaman (1 hingga 398)
    for page in range(1, 399):
        url = url_head.format(page)  # Format URL dengan nomor halaman
        try:
            # Membaca tabel dari URL
            dfs = pd.read_html(url)  # Mengambil semua tabel sebagai list
            
            # Memeriksa apakah ada tabel yang ditemukan
            if dfs:
                # Menambahkan DataFrame pertama dari list ke dalam list dataframes
                dataframes.append(dfs[0])  # Ambil tabel pertama jika ada
        except Exception as e:
            print(f"Error pada halaman {page}: {e}")

    # Menggabungkan semua DataFrame menjadi satu
    final_df = pd.concat(dataframes, ignore_index=True)
    final_df['Kode Pos'] = final_df['Kode Pos'].astype(str)
    
    # Menampilkan DataFrame di Streamlit
    with st.expander('Kode Pos di Jawa Barat'):
        st.dataframe(final_df, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://kodepos.co.id/kodepos/jawa-barat')    
        
    with st.expander('Kode Wilayah Jawa Barat'):
        wilayah = {
                    'Nama':['Bogor', 'Sukabumi', 'Cianjur', 'Bandung', 'Garut', 'Tasikmalaya', 'Ciamis',
                        'Kuningan', 'Cirebon', 'Majalengka', 'Sumedang', 'Indramayu', 'Subang', 'Purwakarta',
                        'Karawang', 'Bekasi', 'Bandung Barat', 'Pangandaran', 'Kota Bogor', 'Kota Sukabumi',
                        'Kota Bandung', 'Kota Cirebon', 'Kota Bekasi', 'Kota Depok', 'Kota Cimahi',
                        'Kota Tasikmalaya', 'Kota Banjar'],
                    'Kode':['3201', '3202', '3203', '3204', '3205', '3206', '3207', '3208', '3209', '3210', 
                            '3211', '3212', '3213', '3214', '3215', '3216', '3217', '3218', '3271', '3272',
                            '3273', '3274', '3275', '3276', '3277', '3278', '3279']
                }
        
        df2 = pd.DataFrame(wilayah)

        # Mengambil daftar nama untuk opsi selectbox
        pilihan = df2['Nama'].tolist()

        # Membuat selectbox
        wilayah_terpilih = st.selectbox('Pilih Kabupaten/Kota:', pilihan)

        # Mengambil kode berdasarkan nama yang dipilih
        kodewilayah = df2.loc[df2['Nama'] == wilayah_terpilih, 'Kode'].values[0]

        url2 = f'https://data.jabarprov.go.id/api-backend/bigdata/disdukcapil_2/od_18275_jumlah_penduduk_berdasarkan_desakelurahan_v1?limit=1000&skip=0&where={{"bps_kode_kabupaten_kota":["{kodewilayah}"]}}'

        response = requests.get(url2)
        
        data2 = response.json()
        
        df3 = pd.DataFrame(data2['data'])
        df3 = df3[['kode_provinsi', 'nama_provinsi', 'bps_kode_kabupaten_kota', 'bps_nama_kabupaten_kota',
                   'bps_kode_kecamatan', 'bps_nama_kecamatan', 'kemendagri_kode_kecamatan', 
                   'kemendagri_nama_kecamatan', 'kemendagri_kode_desa_kelurahan',
                   'kemendagri_nama_desa_kelurahan', 'bps_kode_desa_kelurahan', 'bps_nama_desa_kelurahan']]
        df3 = df3.astype(str)
                
        kec = df3['bps_nama_kecamatan'].unique()
        kec2 = st.selectbox('Filter Kecamatan', kec)
        
        if kec2:
            df4 =df3[df3['bps_nama_kecamatan'] == kec2]
            
            st.dataframe(df4, hide_index=True, use_container_width=True)
        
            st.caption('Sumber: https://opendata.jabarprov.go.id/id/dataset/jumlah-penduduk-berdasarkan-desakelurahan-di-jawa-barat')

st.warning('Baca Pedoman: https://drive.google.com/file/d/1B37k_35MENcx6MQ5UWmnV-EleC-derH0/view?usp=sharing')

st.divider()
st.write('@Forum Satu Data Kota Bandung')