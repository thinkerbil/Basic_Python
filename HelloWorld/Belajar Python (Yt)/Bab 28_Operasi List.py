# OPERASI LIST

# 1. Mengetahui Banyaknya suatu Item pada List --> var.count(item yang dicari)
list_angka = [1,2,4,3,7,8,3,9,1,6,5,4,2,7,9]
banyaknya_angka_4 = list_angka.count(4)
print(f'List angka = {list_angka}')
print(f'Banyaknya angka 4 pada list: {banyaknya_angka_4}\n')


# 2. Mencari Indeks suatu item --> var.index(item yang dicari)
list_nama = ['Tatang','Dudung','Ucok','Asep','Butet','Munaroh']
indeks_asep = list_nama.index('Asep')
indeks_dudung = list_nama.index('Dudung')
indeks_munaroh = list_nama.index('Munaroh')
print(f'List nama = {list_nama}')
print(f'Indeks dari Asep pada list: {indeks_asep}')
print(f'Indeks dari Dudung pada list: {indeks_dudung}')
print(f'Indeks dari Munaroh pada list: {indeks_munaroh}\n')


# 3. Mengurutkan List dari yang terkecil --> var.sort()  --> ga usah buat variabel baru
list_angka = [1,2,4,3,7,8,3,9,1,6,5,4,2,7,9]
print(f'List angka sebelum urut terkecil = {list_angka}')
list_angka.sort()
print(f'List angka setelah urut terkecil = {list_angka}\n')

list_nama = ['Tatang','Dudung','Ucok','Asep','Butet','Munaroh']
print(f'List nama sebelum urut terkecil = {list_nama}')
list_nama.sort()
print(f'List nama setelah urut terkecil = {list_nama}\n')


# 4. Mengurutkan List dari yang terbesar --> var.reverse()
list_angka = [1,2,4,3,7,8,3,9,1,6,5,4,2,7,9]
print(f'List angka sebelum urut terbesar = {list_angka}')
list_angka.reverse()
print(f'List angka setelah urut terbesar = {list_angka}\n')

list_nama = ['Tatang','Dudung','Ucok','Asep','Butet','Munaroh']
print(f'List nama sebelum urut terbesar = {list_nama}')
list_nama.reverse()
print(f'List nama setelah urut terbesar = {list_nama}\n')




