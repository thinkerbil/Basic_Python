# 1. Menyambung String
nama_depan1 = 'Sakura'
nama_tengah1 = 'Nabila'
nama_belakang1 = 'Haruka'
nama_lengkap_1 = f'{nama_depan1} {nama_tengah1} {nama_belakang1}'
print(f'Nama 1: {nama_lengkap_1}')

nama_depan2 = 'Caca'
nama_tengah2 = 'D'
nama_belakang2 = 'Kost'
nama_lengkap_2 = nama_depan2 + ' ' + nama_tengah2 + "'" + nama_belakang2
print(f'Nama 2: {nama_lengkap_2}') 


# 2. Menghitung Panjang String
panjang_nama_1 = len(nama_lengkap_1)
print(f'Panjang Nama 1: {panjang_nama_1}')
panjang_nama_2 = len(nama_lengkap_2)
print(f'Panjang Nama 2: {panjang_nama_2}')

print()


# 3. Operator Untuk String

# Ngecek Ketersediaan Suatu Karakter di Suatu String
# in
b = 'b'
cek = b in nama_tengah1
print(f'Huruf "b" ada di {nama_tengah1}? = {cek} --> "in"')

s = 's'
cek = s in nama_depan1
print(f'Huruf "s" ada di {nama_depan1}? = {cek} --> "in"')

# not in
D = 'D'
cek = D not in nama_lengkap_2
print(f'Huruf D ada di {nama_lengkap_2}? = {cek}  --> "not in"')

print()


# Mengulang String
print('HAHA'*10)
print(10*'HAHA')

print()


# Indexing --> depan: dimulai dari 0, belakang: dimulai dari -1, spasi dihitung
print(f'Indeks ke-0 dari "{nama_lengkap_1}": {nama_lengkap_1[0]}')
print(f'Indeks ke-1 dari "{nama_lengkap_1}": {nama_lengkap_1[1]}')
print(f'Indeks ke-7 dari "{nama_lengkap_1}": {nama_lengkap_1[7]}')
print(f'Indeks ke-(-1) dari "{nama_lengkap_1}": {nama_lengkap_1[-1]}')
print(f'Indeks ke-(-2) dari "{nama_lengkap_1}": {nama_lengkap_1[-2]}')
print(f'Indeks ke-(-5) dari "{nama_lengkap_1}": {nama_lengkap_1[-5]}')

print(f'Indeks ke-0 dari "{nama_lengkap_2}": {nama_lengkap_2[0]}')
print(f'Indeks ke-6 dari "{nama_lengkap_2}": {nama_lengkap_2[6]}')
print(f'Indeks ke-(-1) dari "{nama_lengkap_2}": {nama_lengkap_2[-1]}')
print(f'Indeks ke-(-2) dari "{nama_lengkap_2}": {nama_lengkap_2[-2]}')
print(f'Indeks ke-(-6) dari "{nama_lengkap_2}": {nama_lengkap_2[-6]}')

# Index Rentang [dari:sampai+1:loncat]
print(f'Indeks ke-[0:3] dari "{nama_lengkap_1}": {nama_lengkap_1[0:4]}')
print(f'Indeks ke-[3:8] dari "{nama_lengkap_1}": {nama_lengkap_1[3:9]}')
print(f'Indeks ke-[0,2,4,6,12] dari "{nama_lengkap_1}": {nama_lengkap_1[0:13:2]}  --> loncat dua karakter')

print()


# Item paling kecil
print(f'Karakter paling kecil di "{nama_lengkap_1}": {min(nama_lengkap_1)}')
print(f'Karakter paling besar di "{nama_lengkap_1}": {max(nama_lengkap_1)}')

# cek code: Aschii Code
cek_code = ord(" ")
print(f'ASCII CODE untuk spasi: {cek_code}')
cek_huruf = 117
print(f'Huruf dengan ASCII CODE 117: {chr(cek_huruf)}')


# Method String
# Hitung banyaknya suatu karakter
a = nama_lengkap_1.count("a")
print(f'Jumlah huruf "a" di "{nama_lengkap_1}": {a}')




