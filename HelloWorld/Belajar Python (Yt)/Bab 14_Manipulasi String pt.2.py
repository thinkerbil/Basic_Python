# Operator Method String

nama = 'Sakura Haruka'
print(f'Nama: {nama}')

# 1. Hitung banyaknya suatu karakter (output: string)
cek_count = nama.count("a")
print(f'Jumlah huruf "a" di "{nama}": {cek_count}\n')



print(f'Nama: {nama}')


# 2. Upper case (output: string)
nama_upper = nama.upper()
print(f'Nama: {nama_upper} --> di-upper case')


# 3. Lower Case (output: string)
nama_lower = nama.lower()
print(f'Nama: {nama_lower} --> di-lower case.\n')



# 4. Pengecekan Dengan "is..." Methods

# Pengecekan Upper case/Lower case (output: BOOLEAN --> Konversi ke STRING jika terjadi error)
panggil = 'BRO!'
print(f'Salam: {panggil}')

cek_isupper = panggil.isupper()
print(f'"{panggil}" is upper = {cek_isupper} ')

cek_islower = panggil.islower()
print(f'"{panggil}" is lower = {cek_islower}\n')



# .isalpha()  --> ngecek string: semuanya huruf
# .isalnum()  --> ngecek string: huruf/angka (spasi tidak dihitung)
# .isdecimal()  --> ngecek string: semuanya angka
# .isspace()  --> ngecek string: spasi, tab, newline
# .istitle()  --> ngecek string: semua kata diawali kapital


# contoh 1
nama_depan = 'Kaji'
nama_tengah = 'Ren'
umur = 17
result = f'{nama_depan}{nama_tengah}{umur}'
print(f'Nama & Umur: {result}')

cek_isalpha = result.isalpha()
print(f'"{result}" is alpha / huruf semua = {cek_isalpha}')

cek_isalnum = result.isalnum()
print(f'"{result}" is alnum / huruf or angka = {cek_isalnum}')

cek_isdecimal = result.isdecimal()
print(f'"{result}" is decimal / angka semua = {cek_isdecimal}')

cek_isspace = result.isspace()
print(f'"{result}" is space / ada spasi = {cek_isspace}')

cek_istitle = result.istitle()
print(f'"{result}" is title / awalan huruf kapital = {cek_istitle}\n')




# contoh 2
nama = 'Sakura Haruka'
print(f'Nama: {nama}')

cek_isalpha = nama.isalpha()
print(f'Apakah "{nama}" huruf semua?: {cek_isalpha}') # Karena ada spasi, dianggap bukan huruf semua

cek_isalnum = nama.isalnum()
print(f'Apakah "{nama}" huruf or angka?: {cek_isalnum}') # Karena ada spasi, dianggap bukan huru/angka

cek_isdecimal = nama.isdecimal()
print(f'Apakah "{nama}" angka semua?: {cek_isdecimal}')

cek_isspace = nama.isspace()
print(f'Apakah "{nama}" merupakan spasi: {cek_isspace}')

cek_istitle = nama.istitle()
print(f'Apakah "{nama}" awalan huruf kapital?: {cek_istitle}\n')



# contoh 3
angka = 123456789
angka_str = str(angka)
print(f'Angka: {angka_str}')

cek_isalpha = angka_str.isalpha()
print(f'Apakah "{angka_str}" huruf semua?: {cek_isalpha}')

cek_isalnum = angka_str.isalnum()
print(f'Apakah "{angka_str}" huruf/angka?: {cek_isalnum}')

cek_isdecimal = angka_str.isdecimal()
print(f'Apakah "{angka_str}" angka semua?: {cek_isdecimal}')

cek_isspace = angka_str.isspace()
print(f'Apakah "{angka_str}" merupakan spasi?: {cek_isspace}')

cek_istitle = angka_str.istitle()
print(f'Apakah "{angka_str}" awalan huruf kapital?: {cek_istitle}\n')




# .capitalize() --> huruf pertama di str jadi Uppercase
print('ayam goreng enak'.capitalize())
print('AYAM GORENG ENAK'.capitalize())

# .swapcase() --> uppercase jadi lower case, dan sebaliknya
print('Ayam Goreng Enak'.swapcase())
print('AYAM goreng ENak\n'.swapcase())




# 5. Cek komponen dgn: .startswith() & .endswith()
cek_start = 'Kenji Ren'.startswith("Kenji")
print(f'"Kenji Ren" start with "Kenji": {cek_start}')
cek_start = 'Kenji Ren'.startswith('kenji')
print(f'"Kenji Ren" start with "kenji": {cek_start}')

cek_end = 'Kenji Ren'.endswith("Ren")
print(f'"Kenji Ren" end with "Ren": {cek_end}')
cek_end = 'Kenji Ren'.endswith('ren')
print(f'"Kenji Ren" end with "ren": {cek_end}\n')




# 6. Menggabung dan memisah komponen

# Gabung: 'karakter penggabung'.join(variabel)
kata_terpisah = ['Sakura', 'Haruka']
print(kata_terpisah)
gabung = '&'.join(kata_terpisah)
print(gabung)

gabung = ' & '.join(kata_terpisah)
print(gabung)

gabung = ' kiw '.join(kata_terpisah)
print(f'{gabung}\n')



# Pisah: variabel.split('kata yang mau diilangin')
kata_tergabung = 'SakuradanHaruka'
print(kata_tergabung)
pisah = kata_tergabung.split('dan')
print(f'{pisah} --> menghilangkan "dan"')

kata_tergabung = 'Matahari Terbenam dari Barat'
print(kata_tergabung)
pisah = kata_tergabung.split(' ')
print(f'{pisah} --> menghilangkan spasi.\n')




# 7. Alokasi karakter: .rjust(), .ljust(), .center()

# Rata kanan
rata_kanan = 'kanan'.rjust(10)
print(f'"{rata_kanan}" --> rata kanan dgn spasi')

rata_kanan = 'kanan'.rjust(10,"=")
print(f'"{rata_kanan}" --> rata kanan dgn char =')

# Rata Kiri
rata_kiri = 'kiri'.ljust(10)
print(f'"{rata_kiri}" --> rata kiri dgn spasi')

rata_kiri = 'kiri'.ljust(10,'=')
print(f'"{rata_kiri}" --> rata kiri dgn char =')

# Rata tengah
rata_tengah = 'tengah'.center(10)
print(f'"{rata_tengah}" --> rata tengah dengan spasi')

rata_tengah = 'tengah'.center(10,'=')
print(f'"{rata_tengah}" --> rata tengah dgn char =')


# 8. Menghapus Alokasi Karakter: .strip()
hapus_rataan = rata_tengah.strip('=')
print(f'{hapus_rataan}  --> menghapus = \n')













