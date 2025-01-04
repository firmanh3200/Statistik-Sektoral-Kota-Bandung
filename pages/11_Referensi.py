import streamlit as st

st.set_page_config(layout='wide')

st.header('Daftar Pustaka', divider='rainbow')

st.write('1.	Undang-Undang Republik Indonesia Nomor 23 Tahun 2014 tentang Pemerintahan Daerah;')
st.write('2.	Undang-Undang Republik Indonesia Nomor 16 Tahun 1997 tentang Statistik;')
st.write('3.	Peraturan Pemerintah Nomor 51 Tahun 1999 tentang Penyelenggaraan Statistik;')
st.write('4.	Peraturan Pemerintah Nomor 13 Tahun 2019 tentang Laporan dan Evaluasi \
    Penyelenggaraan Pemerintah Daerah;')
st.write('5.	Peraturan Pemerintah Nomor 13 Tahun 2024 tentang Jenis dan Tarif atas \
    Jenis Penerimaan Negara Bukan Pajak yang Berlaku pada Badan Pusat Statistik;')
st.write('6.	Peraturan Presiden Nomor 39 Tahun 2019 tentang Satu Data Indonesia;')
st.write('7.	Peraturan Presiden Nomor 95 Tahun 2018 tentang Sistem Pemerintahan Berbasis Elektronik;')
st.write('8.	Peraturan Badan Pusat Statistik Nomor 2 Tahun 2019 tentang Persyaratan \
    dan Tata Cara Pengenaan Tarif Rp0,00 (Nol Rupiah) Terhadap Pihak Tertentu \
        atas Penerimaan Negara Bukan Pajak yang Berlaku pada Badan Pusat Statistik;')
st.write('9.	Peraturan Badan Pusat Statistik Nomor 4 Tahun 2019 tentang Norma, Standar, \
    Prosedur, dan Kriteria Penyelenggaraan Statistik Sektoral oleh Pemerintah Daerah;')
st.write('10.	Peraturan Badan Pusat Statistik Nomor 4 Tahun 2020 tentang Petunjuk Teknis Standar Data Statistik;')
st.write('11.	Peraturan Badan Pusat Statistik Nomor 5 Tahun 2020 tentang Petunjuk Teknis Metadata Statistik;')
st.write('12.	Peraturan Badan Pusat Statistik Nomor 3 Tahun 2022 tentang Evaluasi Penyelenggaraan Statistik Sektoral;')
st.write('13.	Peraturan Menteri Komunikasi dan Informatika Nomor 1 Tahun 2023 tentang \
    Interoperabilitas Data dalam Penyelenggaraan Sistem Pemerintahan Berbasis \
        Elektronik dan Satu Data Indonesia;')
st.write('14.	Peraturan Menteri Komunikasi dan Informatika Nomor 20 Tahun 2016 tentang \
    Perlindungan Data Pribadi dalam Sistem Elektronik;')
st.write('15.	Peraturan Walikota Bandung Nomor 11 Tahun 2023 tentang Satu Data Kota Bandung;')
st.write('16.	Peraturan Walikota Bandung Nomor 9 Tahun 2024 tentang Kedudukan, \
    Susunan Organisasi, Tugas dan Fungsi serta Tata Kerja Dinas Daerah Kota Bandung;')
st.write('17.	Peraturan Walikota Bandung Nomor 10 Tahun 2024 tentang Kedudukan, \
    Susunan Organisasi, Tugas dan Fungsi serta Tata Kerja Badan Daerah Kota Bandung;')
st.write('18.	Peraturan Walikota Bandung Nomor 11 Tahun 2024 tentang Lembaga \
    Kemasyarakatan Kelurahan di Kota Bandung;')
st.write('19.	Peraturan Walikota Bandung Nomor 1407 Tahun 2016 tentang Kedudukan, \
    Susunan Organisasi, Tugas dan Fungsi serta Tata Kerja Kecamatan dan \
        Kelurahan di Lingkungan Pemerintah Kota Bandung.')
st.write('20. Peraturan Daerah Kota Bandung Nomor 3 Tahun 2021 tentang Perubahan \
    Atas Peraturan Daerah Kota Bandung Nomor 8 Tahun 2016 Tentang Pembentukan \
        Dan Susunan Perangkat Daerah Kota Bandung')
st.write('21. Keputusan Menteri Perdagangan Nomor 1544 Tahun 2024 tentang Pedoman Penyelenggaraan \
    Statistik Sektoral di Kementerian Perdagangan')
st.write('22. Petunjuk Pelaksanaan dan Petunjuk Teknis Penyelenggaraan Statistik Sektoral Kabupaten Ciamis')
st.write('23. Pedoman Penyelenggaraan Statistik Sektoral Kementerian Pariwisata dan Ekonomi Kreatif')
st.write('24. Pedoman Penyelenggaraan Statistik Sektoral di Lingkup Pemerintah Kota Malang')
st.write('25. Pedoman Penyelenggaraan Statistik Sektoral di Lingkungan Lembaga Kebijakan Pengadaan \
    Barang/Jasa Pemerintah')
st.write('26. Pedoman Penyelenggaraan Statistik Lingkungan Hidup dan Kehutanan')
st.write('27. Panduan Operasional Penghimpunan dan Pengelolaan Metadata Kegiatan Statistik Sektoral/Khusus. \
    https://drive.google.com/file/d/13EmZR8Z9Tp3yEa71iTZKz-KSrE9bKtFr/view?usp=sharing')

st.subheader("", divider='green')

# Menambahkan widget Galichat
chat_script = """
<script src="https://cdn.botpress.cloud/webchat/v2.2/inject.js"></script>
<script src="https://files.bpcontent.cloud/2025/01/04/03/20250104035620-PTG96A7D.js"></script>
"""

# Menyisipkan kode HTML ke dalam aplikasi Streamlit
st.components.v1.html(chat_script, height=600)