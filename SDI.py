import streamlit as st

st.set_page_config(layout='wide')

st.title(':green[SATU DATA KOTA BANDUNG]')

st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

with st.expander('TUJUAN'):
    st.success('Tujuan: Meningkatkan tata kelola data pemerintah agar data yang dihasilkan akurat, mutakhir, terpadu, dapat dipertanggungjawabkan, mudah diakses, dan dapat dibagipakaikan.')
    
with st.expander('PENYELENGGARA'):
    st.success('Pembina Data: Menetapkan standar data, struktur metadata, dan memberikan rekomendasi dalam proses pengumpulan data.')
    st.warning('Walidata: Mengumpulkan, memeriksa kesesuaian data, dan menyebarluaskan data melalui Portal Satu Data Indonesia.')
    st.info('Produsen Data: Menghasilkan dan menyampaikan data serta metadata kepada Walidata.')
    
with st.expander('Portal Satu Data'):
    st.success('Portal Satu Data Indonesia: Media untuk menyebarluaskan data yang dapat diakses oleh instansi pusat dan daerah tanpa biaya.')
    
with st.expander('FORUM SATU DATA'):
    st.write('Forum Satu Data Indonesia: Tempat untuk menyepakati kode referensi dan data induk serta menetapkan instansi yang menjadi walidata atas kode referensi dan data induk tersebut.')
    st.success('Forum Satu Data di tingkat provinsi dan kabupaten/kota memiliki peran penting dalam mengoordinasikan dan menyelesaikan permasalahan terkait penyelenggaraan Satu Data Indonesia (SDI).')
    st.warning('Koordinasi dan Komunikasi: Forum ini menjadi wadah komunikasi dan koordinasi antara Pembina Data, Walidata, Walidata Pendukung, Walidata Kabupaten/Kota, dan Produsen Data untuk menyelesaikan permasalahan penyelenggaraan SDI.')
    st.info('Tingkat Provinsi: Dikoordinasikan oleh Kepala Badan Perencanaan Pembangunan Daerah (Bappeda) Provinsi. Gubernur bertindak sebagai pengarah, dengan Sekretaris Daerah sebagai penanggung jawab dan Bappeda sebagai sekretariat.')
    st.success('Tingkat Kabupaten/Kota: Dikoordinasikan oleh Kepala Bappeda Kabupaten/Kota. Bupati/Walikota bertindak sebagai pengarah, dengan Sekretaris Daerah sebagai penanggung jawab dan Bappeda sebagai sekretariat.')
    
with st.expander('Apa Topik Utama yang dibahas dalam Rapat Forum Satu Data?'):
    st.write('Dalam rapat Forum Satu Data, beberapa topik utama yang biasanya dibahas meliputi:')
    st.success('Data Prioritas: Menyepakati data prioritas yang diperlukan untuk perencanaan pembangunan daerah. Ini termasuk data yang paling penting dan mendesak untuk dikumpulkan dan dikelola.')
    st.warning('Metadata: Penyusunan metadata untuk indikator kinerja utama perangkat daerah. Metadata ini penting untuk memastikan bahwa data yang dihasilkan berkualitas dan sesuai dengan prinsip Satu Data Indonesia.')
    st.info('Evaluasi dan Monitoring: Melakukan evaluasi dan monitoring terhadap pelaksanaan Satu Data di tingkat daerah. Ini untuk memastikan bahwa data yang dihasilkan akurat, mutakhir, dan dapat dipertanggungjawabkan.')
    st.success('Koordinasi dan Komunikasi: Meningkatkan koordinasi dan komunikasi antara Pembina Data, Walidata, Walidata Pendukung, dan Produsen Data untuk menyelesaikan permasalahan penyelenggaraan Satu Data Indonesia.')
    st.warning('Rencana Aksi: Menyusun dan menetapkan rencana aksi yang terintegrasi antara pusat dan daerah untuk mendukung pencapaian Satu Data Indonesia, termasuk dukungan anggaran dan program kegiatan.')
    st.info('Pemetaan Kesiapan: Pemetaan kesiapan pelaksanaan Forum Satu Data di tingkat kabupaten/kota melalui berbagai alat evaluasi seperti pengisian formulir atau survei.')

st.divider()
st.write('@Forum Satu Data Kota Bandung')