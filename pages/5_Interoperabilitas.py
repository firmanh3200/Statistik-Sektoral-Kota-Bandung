import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import pandas as pd
import requests

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')
st.success('Interoperabilitas Data dalam SPBE dan SDI diatur melalui Peraturan Menteri Komunikasi dan \
            Informatika No. 1 Tahun 2023 tentang Interoperabilitas Data dalam Penyelenggaraan Sistem \
            Pemerintahan Berbasis Elektronik dan Satu Data Indonesia')

# URL unduhan langsung Google Drive
file_id = "1eS1WHd107jTVqgDRZ9-biM0sFW3L86oS"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Mendapatkan gambar dari URL
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Menampilkan gambar di Streamlit
st.image(img, caption='Sumber gambar: Permenkominfo 1 2023')

st.subheader('Apa itu Interoperabilitas?')
st.success('Interoperabilitas Data adalah kemampuan Sistem \
Elektronik dengan Karakteristik yang berbeda untuk \
berbagi pakai Data dan informasi secara terintegrasi \
dalam penyelenggaraan Sistem Pemerintahan Berbasis Elektronik.')

st.info('Layanan Interoperabilitas Data adalah layanan yang disediakan oleh \
    instansi tertentu sesuai dengan tugas dan wewenangnya untuk memberikan \
    Interoperabilitas Data secara andal, akuntabel, dan aman.')

st.subheader('', divider='rainbow')
st.subheader('Prinsip Layanan Interoperabilitas Data')

with st.expander('andal dan aman serta bertanggung jawab'):
    st.success('kemampuan Sistem Elektronik untuk \
            melindungi Penyelenggaraan LID dari gangguan dan \
            ancaman secara fisik dan nonfisik, serta beroperasi \
            sesuai dengan kebutuhan penggunaannya.')
    
with st.expander('dapat digunakan kembali (reusable)'):
    st.success('Karakteristik dari komponen yang dibangun dan \
            dikembangkan agar dapatdimanfaatkan secara \
            berulang tanpa perlu dikembangkan lagi oleh pihak \
            yang membutuhkan.')
    
with st.expander('dapat dibaca (readable)'):
    st.success('Karakteristik dari komponen \
            Interoperabilitas Data yang mudah untuk diakses dan dipahami.')
    
with st.expander('dapat dikembangkan lebih lanjut secara mandiri'):
    st.success('Karakteristik dari komponen Interoperabilitas Data yang memberi \
                kemudahan bagi pengembangan lebih lanjut tanpa perlu melibatkan \
                pengembang awal.')
    
with st.expander('dapat diperiksa (auditable)'):
    st.success('Karakteristik dari komponen Interoperabilitas Data yang memberikan \
                kemudahan bagi yang memiliki kewenangan untuk melakukan pengamatan, \
                verifikasi, pengujian, dan pemeriksaan terhadapnya.')
    
with st.expander('dapat diukur kinerjanya'):
    st.success('Karakteristik dari komponen Interoperabilitas Data \
                yang memberikan kemudahan bagi yang memiliki \
                kewenangan untuk melakukan pengukuran keandalan, \
                kinerja, kualitas, kesesuaian dengan peruntukan dan sasaran.')
    
with st.expander('dapat diawasi dan dinilai tingkat pemanfaatannya'):
    st.success('Karakteristik dari komponen \
                Interoperabilitas Data yang memberikan kemudahan \
                bagi yang memiliki kewenangan untuk melakukan \
                pengukuran berjalannya fungsi sebagaimana mestinya, \
                jumlah layanan yang dimanfaatkan dalam rangka \
                mengukur efektivitas dan efisiensi.')
    
with st.expander('dapat dibagipakaikan antar Sistem Elektronik \
                    yang berbeda Karakteristik'):
    st.success('Karakteristik dari komponen Interoperabilitas Data \
                yang memastikan terjadi pemanfaatan bersama oleh penyelenggara \
                Sistem Elektronik dan Sistem Elektronik yang berbeda, \
                sehingga terwujud keseragaman, keterpaduan, dan efisiensi.')

st.subheader('', divider='green')
st.subheader('Standar Interoperabilitas Data')
lid = pd.read_excel('data/standarlid.xlsx')
kategori = lid['Keterangan'].unique()

terpilih = st.selectbox('Pilih Kategori', kategori)
if terpilih:
    st.warning(f'{terpilih}')
    tabel = lid[lid['Keterangan'] == terpilih]
    st.table(tabel)

st.caption('Selengkapnya: https://drive.google.com/file/d/1IUTVm2H3VvthBQnLLxksEXUV7pTkR1QS/view?usp=sharing')