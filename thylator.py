#library
import streamlit as st

#write
tab1, tab2 = st.tabs(['Home', 'Kalkulator'])

with tab1:
    st.header('Thylator')
    st.subheader('Thytrimetry calculator')
    st.write('Hallo selamat datang di Thylator!!!')
    st.image('Thylator_Logo.jpg', width=300)
    st.divider()
    st.subheader('Normalitas')
    st.write('Normalitas adalah ukuran yang menunjukkan konsentrasi dengan berat setara dalam gram per liter larutan. Normalitas juga dikenal dengan sebagai satuan konsentrasi larutan yang setara. Satuan normalitas  adalah mgrek/mL dan dengan lambing “N” Secara umum, normalitas hampir sama dengan molaritas, molaritas merupakan satuan konsentrasi yang mewakili konsentrasi ion terlarut ataupun senyawa terlarut dalam suatu larutan, sedangkan normalitas satuan konsentrasi yang mewakili konsentrasi molar hanya dari komponen asam atau komponen basa.')
    st.subheader('Molaritas')
    st.write('Molaritas adalah jumlah mol zat terlarut per liter zat pelarut. 1 mol zat terlarut apa pun yang terlarut dalam 1 L pelarut memiliki konsentrasi 1,0 mol/L. Molaritas dipengaruhi oleh volume, suhu, dan tekanan zat pelarut. Jika volume meningkat, suhu juga akan ikut meningkat sehingga molaritas larutan berkurang. Satuan molaritas adalah mol/L dan dengan lambang "M".')
    st.subheader('Kadar(%)')
    st.write('Kadar persen bobot per bobot (b/b) menyatakan jumlah gram zat dalam 100 gram larutan atau campuran. Persen bobot per volume (b/v) menyatakan jumlah gram zat dalam 100 ml larutan, sebagai pelarut digunakan air atau pelarut lain.')
    st.subheader('PPM')
    st.write('PPM adalah satuan untuk menghitung kadar kandungan yang terlarut di dalam air. Satuan konsentrasi PPM disebut parts per million. PPM biasanya digunakan untuk untuk menunjukkan konsentrsi dari suatu larutan. Konsentrasi larutan adalah jumlah zat terlarut yang terdapat dalam suatu volume larutan. Konsentrasi ini dapat diukur dengan berbagai satuan, seperti ppm, mg/L, dan mol/L. PPM sendiri sering digunakan dalam industri, terutama dalam bidang kimia, farmasi, dan lingkungan.')
    st.subheader('pH')
    st.write('Tujuan perhitungan pH untuk mengetahui nilai keasaaman atau kebasaaan dari sebuah larutan. pH (Power of Hydrogen) adalah derajat keasaman atau kebasaan suatu larutan. Larutan netral pH bernilai  7, asam pH bernilai kurang dari 7, dan basa pH bernilai lebih dari 7.')
    st.divider()
    st.header('Kelompok 11')
    st.write('Agmy Permata Muchtar (2219027)')
    st.write('Cahyawati Ameiliyani Putri (2219049)')
    st.write('Cantika Deslia Safitri (2219050)')
    st.write('Maia Maharani Nasita Wibowo (2219103)')
    st.write('Zulthia Kusumawathy (2219189)')
    
with tab2:
    st.header('Kalkulator Titrimetri')
    st.write('Sesuai dengan namanya kalkulator ini berguna untuk perhitungan dalam titrimetri, seperti menghitung Normalitas, Molaritas, Kadar(%) baik b/b atau b/v, Kadar PPM, Penentuan jenis larutan berdasarkan pH, dan perhitungan pH')
    st.divider()
    option = st.selectbox(
    'Silahkan pilih',
    ('Normalitas', 'Molaritas', 'Kadar(%)', 'Kadar(PPM)','Penentuan jenis larutan berdasarkan pH', 'Perhitungan pH'))
    if option=='Normalitas':
        Bobot = st.number_input('Masukkan bobot yang diketahui, dalam satuan mg')
        BE = st.number_input('Masukkan BE sampel, dalam satuan mg/mgrek')
        Vsampel = st.number_input('Masukkan volume sampel, dalam satuan mL')
        FP = st.number_input('Masukkan faktor pengali yang diketahui')
        if st.button('HITUNG'):
            Normalitas = Bobot/(BE*Vsampel*FP)
            st.success(f'Normalitas yang didapat adalah {Normalitas} mgrek/mL')
    
    elif option=='Molaritas':
        Bobot = st.number_input('Masukkan bobot yang diketahui, dalam satuan mg')
        BM = st.number_input('Masukkan BM sampel, dalam satuan mg/mmol')
        Vsampel = st.number_input('Masukkan volume sampel, dalam satuan mL')
        FP = st.number_input('Masukkan faktor pengali yang diketahui')
        if st.button('HITUNG'):
            Molaritas = Bobot/(BM*Vsampel*FP)
            st.success(f'Molaritas yang didapat adalah {Molaritas} mmol/mL')
    
    elif option=='Kadar(%)':
        N = st.number_input('Masukkan normalitas yang diketahui, dalam satuan mgrek/mL')
        FP = st.number_input('Masukkan faktor pengali yang diketahui')
        Volume_titran = st.number_input('Masukkan volume titran yang diketahui, dalam satuan mL')
        BE = st.number_input('Masukkan BE sampel, dalam satuan mg/mgrek')
        Vsampel = st.number_input('Masukkan volume sampel, dalam satuan mL')
        Bobot_sampel = st.number_input('Masukkan bobot sampel yang diketahui, dalam satuan g')
        if st.button('HITUNG DALAM B/V'):
            Kadar = Volume_titran*BE*N*FP*100*0.001/Vsampel
            st.success(f'Kadar % b/v yang didapatkan adalah {Kadar} % b/v')
        if st.button('HITUNG DALAM B/B'):
            Kadar = Volume_titran*BE*N*FP*100*0.001/Bobot_sampel
            st.success(f'Kadar % b/v yang didapatkan adalah {Kadar} % b/b')
            
    elif option=='Kadar(PPM)':       
        Volume_titran = st.number_input('Masukkan volume titran yang diketahui, dalam satuan mL')
        BE = st.number_input('Masukkan BE sampel, dalam satuan mg/mgrek')
        N = st.number_input('Masukkan normalitas yang diketahui, dalam satuan mgrek/mL')
        FP = st.number_input('Masukkan faktor pengali yang diketahui')
        Bobot = st.number_input('Masukkan bobot yang diketahui, dalam satuan Kg')
        if st.button('HITUNG'):
            Kadar_PPM = Volume_titran*BE*N*FP/Bobot
            st.success(f'Kadar PPM yang didapatkan adalah {Kadar_PPM} mg/Kg')
            
            
    elif option=='Penentuan jenis larutan berdasarkan pH':
        #dictionary
        dictPh = {
            'Merah': 'Asam Kuat',
            'Jingga': 'Asam Lemah',
            'Kuning': 'Asam Sangat Lemah',
            'Hijau': 'Netral',
            'Biru': 'Basa Sangat Lemah',
            'Ungu': 'Basa Lemah',
            'Violet': 'Basa Kuat'
        }

        # input dari user
        pH = st.number_input("Masukkan nilai pH nya: ")
        st.write('pH nya adalah ', pH)
        
        #hasil
        def output():
            if pH < 1 or pH > 14:
                st.write("Nilai Ph tidak valid, silahkan masukkan angka mulai dari 1-14")
            elif pH >= 1 and pH <= 3:
                st.write("Nilai Ph memiliki sifat" + dictPh["Merah"], 'dengan warna Merah')
            elif pH >= 3 and pH <= 5:
                st.write("Nilai Ph memiliki sifat " + dictPh["Jingga"], 'dengan warna Jingga')
            elif pH >= 5 and pH <= 6:
                st.write("Nilai Ph memiliki sifat " + dictPh["Kuning"], 'dengan warna Kuning')
            elif pH >= 6 and pH <= 7:
                st.write("Nilai Ph memiliki sifat " + dictPh["Hijau"], 'dengan warna Hijau')
            elif pH >= 7 and pH <= 8:
                st.write("Nilai Ph memiliki sifat " + dictPh["Biru"], 'dengan warna Biru')
            elif pH >= 8 and pH <= 10:
                st.write("Nilai Ph memiliki sifat " + dictPh["Ungu"], 'dengan warna Ungu')
            elif pH >= 10 and pH <= 14:
                st.write("Nilai Ph memiliki sifat " + dictPh["Violet"], 'dengan warna Violet')

        #output
        output()


    elif option=='Perhitungan pH':
        st.write('Setelah melakukan perhitungan secara stoikiometri, silahkan pilih kondisi yang sesuai dengan hasil perhitungan anda')
        option = st.selectbox(
            'Pilih kondisi:',
            ('Sisa Asam', 'Sisa Basa'))
        if option== 'Sisa Asam': 
            mmol = st.number_input('Masukkan jumlah mmol asam yang diketahui, dalam satuan mmol')
            st.write(f'Nilai mmol adalah {mmol} mmol')
            v = st.number_input('Masukkan volume total larutan yang diketahui, dalam satuan mL')
            st.write(f'Nilai volume adalah {v} mL')
            if st.button('HITUNG'):
                H = mmol/v
                import numpy as np
                pH = -1*np.log10(H)
                st.success(f'pH yang didapatkan adalah {pH}')
        if option=='Sisa Basa':
            mmol = st.number_input('Masukkan mmol yang diketahui')
            st.write(f'Nilai mmol adalah {mmol} mmol')
            v = st.number_input('Masukkan volume total larutan yang diketahui, dalam satuan mL')
            st.write(f'Nilai volume adalah {v} mL')
            if st.button('HITUNG'):
                OH=mmol/v
                import numpy as np
                pOH = -1*np.log10(OH)
                pH = 14-(pOH)
                st.success(f'pH yang didapatkan adalah {pH}')