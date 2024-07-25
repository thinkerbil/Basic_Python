# Width and Multiline

nama = 'sakura'
umur = 17
ukuran_sepatu = 40
tempat_lahir = 'Tokyo'

# String standard
print('String Standard'.center(40,"="))
print(f'Nama: {nama}, Umur: {umur}, Tempat Lahir: {tempat_lahir}, Ukuran sepatu: {ukuran_sepatu}\n')

# String Multiline Newline (\n)
print('String Multiline Newline (\\n)'.center(40,"="))
print(f'Nama: {nama}\nUmur: {umur}\nTempat Lahir: {tempat_lahir}\nUkuran Sepatu: {ukuran_sepatu}\n')

# String Multiline Kutip Triplets
print('String Multiline Kutip Triplets'.center(40,"="))
print(f'''
Nama: {nama}
Umur: {umur}
Tempat Lahir: {tempat_lahir}
Ukuran Sepatu: {ukuran_sepatu}
''')

print()

# Mengatur Lebar agar sejajar
print('Mengatur Lebar Agar Sejajar'.center(40,'='))

# Manual
print(f'''
Nama         : {nama}
Umur         : {umur}
Tempat Lahir : {tempat_lahir}
Ukuran Sepatu: {ukuran_sepatu}
''')

# Beri format Tab (\t)
print(f'Nama\t\t: {nama}\nUmur\t\t: {umur}\nTempat Lahir\t: {tempat_lahir}\nUkuran Sepatu\t: {ukuran_sepatu}')

print(f'''
Nama\t\t: {nama}
Umur\t\t: {umur}
Tempat Lahir\t: {tempat_lahir}
Ukuran Sepatu\t: {ukuran_sepatu}
''')

# Mengatur Rata Kanan/Kiri

# Rata Kanan
print(f'''
Nama         : {nama:>8}
Umur         : {umur:>8}
Tempat Lahir : {tempat_lahir:>8}
Ukuran Sepatu: {ukuran_sepatu:>8}
\n''')

# {variabel:n} --> n = jumlah karakter yang bisa digunkanan untuk jarak dgn kata2 setelahnya
# {nama:10} --> oleh karena {nama} = 'sakura' (6 karakter) --> arti dari {nama:10} adalah akan membuat output 'nama' menjadi 10 karakter
# kekurangan karakternya tsb diganti dengan spasi agar menjadi 10 karakter
print(f'Nama: {nama:10} Umur: {umur}')