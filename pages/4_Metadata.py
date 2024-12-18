import streamlit as st

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

st.subheader('METADATA STATISTIK', divider='rainbow')

st.subheader('Metadata Kegiatan Statistik')
st.success('Sekumpulan atribut informasi yang memberikan gambaran / dokumentasi \
            dari penyelenggaraan kegiatan statistik')

with st.expander('Judul Kegiatan'):
    st.info('Judul kegiatan minimal memuat cara pengumpulan data, komponen utama \
            kegiatan, cakupan wilayah, dan periode pelaksanaan.')
    st.warning('Ada kemungkinan, kegiatan statistik yang dilaksanakan oleh suatu OPD, \
            juga dilaksanakan oleh OPD serupa di pemerintahan daerah lainnya. Oleh karena itu \
            kita bisa mencari referensi kegiatan serupa melalui Sistem Rujukan Statistik.')
    st.success('Bingung dalam menentukan Judul Kegiatan? silakan buka tautan: \
                https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=kegiatan')

with st.expander('Cara Pengumpulan Data'):
    st.success('Pencancahan Lengkap adalah Cara pengumpulan data yang dilakukan melalui pencacahan \
            seluruh unit populasi.')
    st.info('Survei adalah Cara pengumpulan data yang dilakukan melalui pencacahan sampel \
            untuk memperkirakan karakteristik suatu populasi.')
    st.warning('Kompilasi Produk Administrasi/ Kompilasi Data Administrasi adalah \
            Cara pengumpulan, pengolahan, penyajian, dan analisis data didasarkan \
            pada catatan administrasi yang ada pada pemerintah, swasta, dan atau masyarakat.')
    st.success('Cara lain seperti: web scraping, API, crowdsourcing, dll sesuai perkembangan TI.')

with st.expander('Tahapan Kegiatan'):
    st.success('Perencanaan -> Pembuatan Desain (Input, Proses, Output) -> Pengumpulan Data -> Pengolahan Data -> \
                Analisis -> Diseminasi Hasil -> Evaluasi')
    
with st.expander('Variabel (Karakteristik) yang Dikumpulkan'):
    st.write('Variabel dapat dilihat dari judul data/ judul tabel yang dihasilkan dari kegiatan tersebut, \
                misalnya :blue[Jumlah Korban Kekerasan terhadap Anak Perempuan Berdasarkan Kelompok \
                    Usia dan Kabupaten/Kota di Jawa Barat], berarti memerlukan variabel-variabel :blue[korban kekerasan], \
                    :blue[Jenis Kelamin], :blue[Kelompok Usia], dan :blue[Kabupaten/Kota].')
    
    st.write('untuk dapat menghasilkan data: :green[Jumlah Sarana dan Prasarana Olahraga Berdasarkan \
            Kabupaten/Kota di Jawa Barat] memerlukan variabel: :green[sarana], :green[prasarana], \
                dan :green[Kabupaten/Kota].')
    
    st.success('untuk lebih mudah dalam melihat variabel adalah dengan melihat langsung dari kuesioner, \
            angket, form, atau instrumen pengumpulan datanya, serta bentuk tabel yang dihasilkan.')
    
with st.expander('Longitudinal Panel'):
    st.success('longitudinal panel adalah metode pengumpulan data yang melibatkan pengamatan berulang \
                terhadap subjek yang sama dalam jangka waktu tertentu.')
    st.write('Contoh Longitudinal Panel:')
    
    st.success('Studi Kesehatan: Penelitian yang melacak kesehatan sekelompok individu selama beberapa \
                tahun untuk mengamati perubahan dalam kondisi kesehatan mereka. Misalnya, sebuah studi \
                yang memantau perkembangan penyakit kronis seperti diabetes atau hipertensi pada \
                sekelompok pasien dari tahun ke tahun.')
    
    st.info('Studi Pendidikan: Penelitian yang mengikuti perkembangan akademik siswa dari sekolah dasar \
            hingga perguruan tinggi. Studi ini dapat mengamati bagaimana faktor-faktor seperti latar \
            belakang keluarga, kualitas sekolah, dan intervensi pendidikan mempengaruhi prestasi akademik siswa.')
    
    st.warning('Studi Ekonomi: Penelitian yang mengamati perubahan pendapatan dan pekerjaan sekelompok \
            rumah tangga selama beberapa dekade. Studi ini dapat membantu memahami dinamika ekonomi, \
            mobilitas sosial, dan dampak kebijakan ekonomi terhadap kesejahteraan rumah tangga.')
    
    st.write('Studi Sosial: Penelitian yang memantau perubahan sikap dan perilaku politik sekelompok \
            individu dari waktu ke waktu. Misalnya, survei tahunan yang mengukur perubahan pandangan \
            politik dan partisipasi pemilih dalam populasi tertentu.')
    
with st.expander('Cross Sectional'):
    st.success('cross-sectional adalah metode pengumpulan data yang dilakukan pada satu titik waktu \
                tertentu untuk mendapatkan gambaran dari populasi atau sampel pada saat itu.')
    
    st.write('Contoh Cross Sectional:')
    
    st.success('Studi Pendidikan: Mengumpulkan data tentang prestasi akademik siswa pada satu waktu \
                tertentu. Contohnya, survei yang dilakukan untuk mengetahui hubungan antara kebiasaan \
                belajar dan hasil ujian siswa di sekolah menengah pada semester ini.')
    
    st.info('Penelitian Sosial: Mengumpulkan data tentang sikap dan perilaku masyarakat terhadap isu \
            tertentu. Misalnya, survei yang dilakukan untuk mengetahui pandangan masyarakat terhadap \
            kebijakan pemerintah tentang ketenagakerjaan pada tahun tertentu.')
    
    st.warning('Studi Konsumen: Mengumpulkan data tentang preferensi konsumen terhadap produk tertentu \
            pada satu waktu. Contohnya, survei yang dilakukan oleh perusahaan makanan untuk mengetahui \
                preferensi rasa es krim di kalangan remaja pada musim panas tahun ini.')
    
with st.expander('Analisis Inferensia'):
    st.success('Analisis Inferensia adalah Analisis yang bertujuan untuk menarik kesimpulan pada sampel, yang \
                digunakan untuk digeneralisir ke populasi. Analisis yang bertujuan untuk \
                menarik kesimpulan berdasarkan data hasil pengolahan menggunakan \
                metode statistik yang lebih mendalam, seperti anova, korelasi, regresi, chisquare, faktor, \
                cluster, dan diskriminan.')
    
st.subheader('', divider='rainbow')
with st.expander('Sistem Rujukan Statistik (SIRUSA)'):
    st.link_button("Metadata Statistik Sektoral", url="https://sirusa.bps.go.id/sirusa/index.php/sektoral/index")

    kol1, kol2, kol3, kol4 = st.columns(4)
    with kol1:
        st.link_button("Metadata Statistik Khusus", url="https://sirusa.bps.go.id/sirusa/index.php/khusus/index")
    with kol2:
        st.link_button("Metadata Statistik Dasar", url="https://sirusa.bps.go.id/sirusa/index.php/dasar/index")
    with kol3:
        st.link_button("Glosarium", url="https://sirusa.bps.go.id/sirusa/index.php/istilah/index")
    with kol4:
        st.link_button("Tata Cara Pelaksanaan Survei", url="https://sirusa.bps.go.id/sirusa/index.php/solusi/page?view=konsep&tab=1")
        
st.divider()
st.write('@Forum Satu Data Kota Bandung')