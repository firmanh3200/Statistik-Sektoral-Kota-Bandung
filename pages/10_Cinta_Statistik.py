import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.header('Pembinaan Kelurahan Cinta Statistik')
st.header('Kota Bandung', divider='rainbow')

st.warning('Potensi Data Kelurahan untuk dibina, dijaga, dan ditingkatkan kualitasnya')

# Function to fetch data from URL based on selected code
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.read_html(response.text)  # Read HTML tables from the response
        return data[0]  # Assuming the data is in the first table
    else:
        st.error("Gagal mengambil data. Status code: {}".format(response.status_code))
        return None

@st.cache_data    
def kamus():
    mfd3200 = pd.read_csv('data/mfd2023.csv', sep=',', encoding='utf-8')
    
    mendagri = pd.read_csv('data/kdkec_mendagri.csv', sep=',', encoding='utf-8')
    
    return mfd3200, mendagri
mfd3200, mendagri = kamus()

with st.container(border=True):
    kol1, kol2, kol3 = st.columns(3)
    with kol1:
        mfd = mfd3200[mfd3200['idkab'] == 3273]
        kabkot = mfd['idkab'].unique().tolist()
        kabterpilih1 = st.selectbox("Filter IDKAB", kabkot, key='kabkot1')
    with kol2:
        kec = mfd[mfd['idkab'] == kabterpilih1]['idkec'].unique().tolist()
        kecterpilih1 = st.selectbox("Filter IDKEC", kec, key='kec1')
    with kol3:
        desa = mfd[mfd['idkec'] == kecterpilih1]['iddesa'].unique().tolist()
        desaterpilih = st.selectbox("Filter IDDESA", desa, key='desa1')    

st.subheader('', divider='green')

# Main Streamlit app
@st.cache_data    
def main():
    with st.expander('DATA POKOK KELURAHAN'):
        st.header("DATA POKOK KELURAHAN", divider='rainbow')
        st.success("Sumber: e-prodeskel Kemendagri")
                
        if kol1 and kol2 and kol3:
            url = f"https://e-prodeskel.kemendagri.go.id/datapokok/data.php?kodesa={desaterpilih}"

            # Fetch data based on selected code
            tables = pd.read_html(url)

            df0 = tables[0]
            df1 = tables[1]
            df2 = tables[2]
            df3 = tables[3]
            #df4 = tables[4]

            tabel0 = pd.DataFrame(df0)
            tabel1 = pd.DataFrame(df1)
            tabel2 = pd.DataFrame(df2)
            tabel3 = pd.DataFrame(df3)
            #tabel4 = pd.DataFrame(df4)

            gabungan = pd.concat([tabel0, tabel1, tabel2, tabel3], axis=1)
            
            st.dataframe(tabel0, use_container_width=True, hide_index=True)
            st.dataframe(tabel1, use_container_width=True, hide_index=True)
            st.dataframe(tabel2, use_container_width=True, hide_index=True)
            st.dataframe(tabel3, use_container_width=True, hide_index=True)
            #st.dataframe(tabel4, use_container_width=True, hide_index=True)
        
        st.link_button("Lihat Sumber Data", url=f"https://e-prodeskel.kemendagri.go.id/datapokok/data.php?kodesa={desaterpilih}")

if __name__ == '__main__':
    main()
    
@st.cache_data    
def total_penduduk():
    with st.expander('TOTAL PENDUDUK'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_kelurahan"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'jumlah_penduduk', 'tahun', 'semester']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-kelurahan')
            
if __name__ == '__main__':
    total_penduduk()

@st.cache_data    
def jenis_pekerjaan():
    with st.expander('JENIS PEKERJAAN PENDUDUK'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_jenis_pekerjaan?sort=id%3Aasc&page=1&per_page=22000&where=%7B%7D&where_or=%7B%7D"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'jenis_pekerjaan', 'jumlah_penduduk', 'tahun', 'semester']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-jenis-pekerjaan')
            
if __name__ == '__main__':
    jenis_pekerjaan()

@st.cache_data    
def agama():
    with st.expander('AGAMA PENDUDUK'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_agama_4?sort=id%3Aasc&page=1&per_page=15000&where=%7B%7D&where_or=%7B%7D"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'agama', 'jumlah_penduduk', 'tahun', 'semester']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-agama-4')
            
if __name__ == '__main__':
    agama()

@st.cache_data    
def goldar():
    with st.expander('GOLONGAN DARAH PENDUDUK'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_golongan_darah_3?sort=id%3Aasc&page=1&per_page=28000&where=%7B%7D&where_or=%7B%7D"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'tipe_goldar', 'jumlah_penduduk', 'tahun', 'semester']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-golongan-darah-3')
            
if __name__ == '__main__':
    goldar()

@st.cache_data    
def jenis_pendidikan():
    with st.expander('JENIS PENDIDIKAN PENDUDUK'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_jenis_pendidikan_2?sort=id%3Aasc&page=1&per_page=23000&where=%7B%7D&where_or=%7B%7D"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'jenis_pendidikan', 'jumlah_penduduk', 'tahun', 'semester']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-jenis-pendidikan-2')
            
if __name__ == '__main__':
    jenis_pendidikan()

@st.cache_data    
def usia_pendidikan():
    with st.expander('USIA PENDIDIKAN PENDUDUK'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_usia_pendidikan?sort=id%3Aasc&page=1&per_page=14000&where=%7B%7D&where_or=%7B%7D"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'kelompok_usia_pendidikan', 'jumlah_penduduk', 'tahun', 'semester']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-usia-pendidikan')
            
if __name__ == '__main__':
    usia_pendidikan()

@st.cache_data    
def jenis_kelamin():
    with st.expander('JENIS KELAMIN PENDUDUK'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_jenis_kelamin_3?sort=id%3Aasc&page=1&per_page=5000&where=%7B%7D&where_or=%7B%7D"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'jenis_kelamin', 'jumlah_penduduk', 'tahun', 'semester']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-jenis-kelamin-3')
            
if __name__ == '__main__':
    jenis_kelamin()

@st.cache_data    
def kk():
    with st.expander('KEPALA KELUARGA'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_kepala_keluarga_berdasarkan_kelurahan_di_kota_bandung?sort=id%3Aasc&page=1&per_page=3000&where=%7B%7D&where_or=%7B%7D"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'jumlah_kk', 'tahun', 'semester']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-kepala-keluarga-berdasarkan-kelurahan-di-kota-bandung')
            
if __name__ == '__main__':
    kk()

@st.cache_data    
def stunting():
    with st.expander('BALITA STUNTING'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_kesehatan/jumlah_balita_stunting_berdasarkan_kelurahan_di_kota_bandung?sort=id%3Aasc&page=1&per_page=1000&where=%7B%7D&where_or=%7B%7D"

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
        
        penduduk_kelurahan = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df_penduduk = penduduk_kelurahan[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'keterangan', 'jumlah_balita', 'tahun']]
        st.dataframe(df_penduduk, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-balita-stunting-berdasarkan-kelurahan-di-kota-bandung')
            
if __name__ == '__main__':
    stunting()

@st.cache_data    
def tpu():
    with st.expander('TAMAN PEMAKAMAN UMUM'):
        # URL API Open Data
        url = "https://opendata.bandung.go.id/api/bigdata/dinas_cipta_karya_bina_konstruksi_dan_tata_ruang/luas_lahan_pemakaman_menurut_jenis_tpu_di_kota_bandung?sort=id%3Aasc&page=1&per_page=40&where=%7B%22tahun%22%3A%5B%222021%22%5D%7D&where_or=%7B%7D"

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
        
        df2 = df[df['bps_kode_desa_kelurahan'] == desaterpilih]
        df3 = df2[['kemendagri_kode_desa_kelurahan', 'bps_kode_desa_kelurahan',
                                        'kemendagri_nama_desa_kelurahan', 'tahun_berdiri', 'keterangan', 
                                        'luas', 'satuan']]
        st.dataframe(df3, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/luas-lahan-pemakaman-menurut-jenis-tpu-di-kota-bandung')
            
if __name__ == '__main__':
    tpu()

def lainnya():
    with st.expander('LAINNYA'):
        st.caption('https://opendata.bandung.go.id/dataset/jumlah-keluarga-di-data-terpadu-kesejahteraan-sosial-dtks-berdasarkan-kelurahan-di-kota-bandung')
        st.caption('https://opendata.bandung.go.id/dataset/jumlah-individu-di-data-terpadu-kesejahteraan-sosial-dtks--berdasarkan-kelurahan-di-kota-bandung')
        st.caption('https://opendata.bandung.go.id/dataset/jumlah-rumah-di-kota-bandung-2')
        st.caption('https://opendata.bandung.go.id/dataset/luas-wilayah-kumuh-berdasarkan-kelurahan-di-kota-bandung')
        st.caption('https://opendata.bandung.go.id/dataset/rekap-penilaian-kelurahan-layak-anak-tingkat-kota-bandung-2')
        st.caption('https://opendata.bandung.go.id/dataset/koperasi-di-kota-bandung')
        st.caption('https://opendata.bandung.go.id/dataset/lokasi-internet-rw-di-kota-bandung')
        st.caption('https://opendata.bandung.go.id/dataset/kelompok-pengolah-hasil-pertanian-di-kota-bandung-2')
        st.caption('https://opendata.bandung.go.id/dataset/kelompok-tani-pangan-di-kota-bandung-2')
        st.caption('https://opendata.bandung.go.id/dataset/kelompok-tani-hortikultura-di-kota-bandung-2')
        st.caption('https://opendata.bandung.go.id/dataset/kelompok-peternakan-di-kota-bandung-2')
        st.caption('https://opendata.bandung.go.id/dataset/kelompok-pembudidaya-ikan-di-kota-bandung-2')
        st.caption('https://opendata.bandung.go.id/dataset/luas-lahan-sawah-berdasarkan-jenis-sawah-dan-kelurahan-di-kota-bandung')
        st.caption('https://opendata.bandung.go.id/dataset/lokasi-kejadian-kebakaran-di-kota-bandung')
    
if __name__ == '__main__':
    lainnya()
    
st.subheader('', divider='rainbow')


kabterpilih5 = 3273
kec5 = mendagri[mendagri['kodekab'] == kabterpilih5]['kodekec'].unique()


def prodeskel():
    st.warning('PRODESKEL KEMENDAGRI')
    tahun = ['2024', '2023', '2022', '2021', '2020', '2019', '2025', '2026', '2027']
    
    kol1, kol2 = st.columns(2)
    with kol1:
        tahunterpilih = st.selectbox('Filter Tahun Laporan', tahun)
    with kol2:
        kecterpilih5 = st.selectbox('Filter Kode Kecamatan Kemendagri', kec5, key='kec5')

    if tahunterpilih and kecterpilih5:
        
        with st.expander("Sarana Prasarana"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/10?kode_daerah={kecterpilih5}"

            tables = pd.read_html(url2)

            df = tables[0]
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)
            
        with st.expander("Pendidikan Penduduk"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/2?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)    
        
        with st.expander("Keluarga Sejahtera"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/6?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)  
        
        with st.expander("Lembaga Kemasyarakatan"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/7?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)      
                    
        with st.expander("Musrenbang"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/8?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)      
        
        with st.expander("Posyandu"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/9?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)
            
        with st.expander("Potensi Iklim"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/11?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)    
        
        with st.expander("Sawah"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/12?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)      

        with st.expander("Penduduk"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/13?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            tabel = pd.DataFrame(df)
            st.dataframe(tabel, hide_index=True, use_container_width=True)        
        
        with st.expander("Lahan Hutan"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/14?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)    
        
        with st.expander("Lahan Perkebunan"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/15?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)     

        with st.expander("Lahan Pertanian"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/16?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)    
        
        with st.expander("Luas Wilayah"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/19?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)
        
        with st.expander("Prasarana Keagamaan"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/20?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)   
        
        with st.expander("Pendidikan Perangkat Desa"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/21?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)  
        
        with st.expander("Air Bersih"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/22?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)
        
        with st.expander("Kesehatan"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/23?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)      
        
        with st.expander("Kominfo"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/24?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)     
        
        with st.expander("RT RW"):
            url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahunterpilih}/data-integrasi-level/34?kode_daerah={kecterpilih5}"

            # Fetch data based on selected code
            tables = pd.read_html(url2)

            df = tables[0]
            
            df = df.drop(columns=df.filter(like='STATUS PEMERITAHAN').columns)
            df = df.drop(columns=df.filter(like='KOTA').columns)
            df = df.drop(columns=df.filter(like='NAMA KECAMATAN').columns)
            
            st.dataframe(df, hide_index=True, use_container_width=True)  
    
        
if __name__ == '__main__':
    prodeskel()

st.subheader('', divider='rainbow')
