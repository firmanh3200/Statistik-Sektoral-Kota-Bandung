import streamlit as st

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('TAHAPAN PELAKSANAAN')

with st.expander('Identifikasi Kebutuhan Data'):
    st.success('Mengidentifikasi kebutuhan data daerah sesuai dengan kebutuhan perencanaan pembangunan daerah.')
    st.warning('Dikoordinasikan oleh Walidata (Diskominfo) dengan melibatkan Produsen Data dari perangkat daerah.')
    
with st.expander('Pengumpulan Data'):
    st.success('Meminta rekomendasi kepada Pembina Data.')
    st.warning('Mengumpulkan data yang telah diidentifikasi sesuai dengan kebutuhan.')
    st.info('Dikoordinasikan oleh Walidata dengan melibatkan Produsen Data dari perangkat daerah.')
    
with st.expander('Pemeriksaan Data'):
    st.success('Memeriksa kesesuaian data yang telah dikumpulkan dengan prinsip Satu Data Indonesia.')
    st.warning('Pemeriksaan ini memastikan bahwa data yang dihasilkan dapat dipertanggungjawabkan dan sesuai dengan standar yang ditetapkan.')
    
with st.expander('Penyusunan Metadata'):
    st.success('Menyusun metadata untuk setiap data yang dikumpulkan. Metadata ini mencakup informasi tentang sumber data, metode pengumpulan, dan kualitas data.')
    st.warning('Metadata membantu dalam memastikan interoperabilitas dan penggunaan data yang lebih efektif.')
    
with st.expander('Penyebarluasan Data'):
    st.success('Menyebarluaskan data melalui Portal Satu Data Indonesia sehingga dapat diakses oleh instansi pusat dan daerah.')
    st.warning('Data yang disebarluaskan harus memenuhi standar dan prinsip Satu Data Indonesia.')
    
with st.expander('Monitoring dan Evaluasi'):
    st.success('Melakukan monitoring dan evaluasi terhadap pelaksanaan Satu Data di tingkat daerah.')
    st.warning('Evaluasi ini bertujuan untuk memastikan bahwa data yang dihasilkan terus memenuhi standar dan dapat digunakan untuk perencanaan pembangunan yang lebih baik.')
    
with st.expander('Rapat Koordinasi'):
    st.success('Mengadakan rapat koordinasi secara berkala untuk membahas dan menyelesaikan berbagai isu terkait data.')
    st.warning('Rapat ini juga digunakan untuk menyepakati langkah-langkah strategis dalam pengelolaan data di daerah.')
    
st.success('Tahapan-tahapan ini dirancang untuk memastikan bahwa data yang dihasilkan oleh pemerintah daerah dapat digunakan secara efektif dalam perencanaan dan evaluasi pembangunan.')

st.divider()
st.write('@Forum Satu Data Kota Bandung')