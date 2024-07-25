# MANIPULASI LIST

# 1. INDEKS
print('INDEKS LIST'.center(40,'='))
# Contoh: ['Anya','Loid','Yor']
# indeks:   0/-3   1/-2   2/-1

list_nama = ['Anya','Loid','Yor']
print(f'Data nama = {list_nama}')
print(f'Indeks ke-0 dari data nama: {list_nama[0]}')
print(f'Indeks ke-1 dari data nama: {list_nama[1]}')
print(f'Indeks ke-(-2) dari data nama: {list_nama[-2]}')
print(f'Indeks ke-(-1) dari data nama: {list_nama[-1]}\n')

list_angka = [1,2,5,7,4,9]
print(f'Data angka = {list_angka}')
print(f'Indeks ke-3 dari data angka: {list_angka[3]}')
print(f'Indeks ke-(-3) dari data angka: {list_angka[-3]}')
print(f'Indeks ke-(-1) dari data angka: {list_angka[-1]}')
print(f'Indeks ke-0 dari data angka: {list_angka[0]}\n')

# 2. MENAMBAH DATA PADA LIST
print('MENAMBAH DATA PADA LIST'.center(40,'='))

list_nama = ['Anya','Loid','Yor']
print(f'Data nama lama = {list_nama}')

# Menambah item pada posisi yang diinginkan --> var.insert(indeks,data yang mau diinput)
list_nama.insert(1,'Yuri')
print(f'Data nama baru = {list_nama}')

list_nama.insert(2,2)
print(f'Data baru: {list_nama}')

list_nama.insert(3,True)
print(f'Data baru: {list_nama}\n')


# Menambah item di akhir --> var.append(data yang mau diinput)
list_nama = ['Anya','Loid','Yor']
print(f'Data nama lama = {list_nama}')
list_nama.append('Forger')
print(f'Data nama baru: {list_nama}')

list_angka = [1,2,5,7,4,9]
print(f'Data angka lama = {list_angka}')
list_angka.append(10)
print(f'Data angka baru: {list_angka}\n')


# Menambah List dgn List --> var.extend([list yang mau diinput])
list_nama = ['Anya','Loid','Yor']
print(f'Data nama lama = {list_nama}')
list_nama.extend(['Sakura','Umemiya','Sho','Togame'])
print(f'Data nama baru: {list_nama}')

list_nama = ['Anya','Loid','Yor']
print(f'Data nama lama = {list_nama}')
list_nama.extend([1,2,3,4,5,6])
print(f'Data nama baru: {list_nama}\n')


# 3. MERUBAH/MENGGANTI DATA --> var[indeks yang mau diubah] = data yang mau menggantikan
print('MENGGANTI DATA'.center(40,'='))

list_nama = ['Anya','Loid','Yor']
print(f'Data nama lama = {list_nama}')
list_nama[0] = 'Yuri'
print(f'Data nama baru: {list_nama}\n')


# 4. MEREMOVE/MENGELUARKAN DATA --> var.remove(data yang mau diremove)
print('MEREMOVE DATA'.center(40,'='))

list_nama = ['Anya','Loid','Yor']
print(f'Data nama lama = {list_nama}')
list_nama.remove('Anya')
print(f'Data nama baru: {list_nama}\n')

# Meremove data paling belakang --> var.pop()
list_nama = ['Anya','Loid','Yor']
print(f'Data nama lama = {list_nama}')
data_terakhir_yang_diremove = list_nama.pop()
print(f'Data nama baru: {list_nama}')
print(f'Data yang diremove: {data_terakhir_yang_diremove}')






