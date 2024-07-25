# COPY LIST

# Copy list --> membuat data baru dgn isi yang identik dgn data sebelumnya / menduplikat data dengan memori yang berbeda


# Contoh
list_nama_1 = ['Sakura','Suo','Umemiya','Togame']
print(f'Data nama 1 = {list_nama_1}')

list_nama_2 = list_nama_1 # var ini punya memori yg sama dgn var list_nama_1 --> hanya membuat var dgn nama baru, tapi data yg dipake sama
print(f'Data nama 2 = {list_nama_2}\n')

# Merubah isi list var pertama
print('Merubah isi var pertama'.center(50,'='))
list_nama_1[1] = 'Budi'
print(f'Data nama 1 = {list_nama_1}')

print(f'Data nama 2 = {list_nama_2} --> ikut berubah.\n') # Tanpa merubah var kedua, tapi isi var kedua ikut berubah karena isi var pertama berubah




# Agar var kedua tidak ikut berubah, maka cara buat variabel kedua adalah meng-copy variabel pertama
print('COPY LIST'.center(50,'='))
print('Copy List Data Pertama Untuk Data Kedua'.center(50,'='))

list_nama_1 = ['Sakura','Suo','Umemiya','Togame']
print(f'Data nama 1 = {list_nama_1}')

list_nama_2 = list_nama_1.copy()
print(f'Data nama 2 = {list_nama_2} --> copy-an data pertama.\n')

# Merubah isi list var pertama
print('Merubah isi var pertama'.center(50,'='))

list_nama_1[1] = 'Budi'
print(f'Data nama 1 = {list_nama_1} --> Index ke-1 diubah jadi "Budi".')

print(f'Data nama 2 = {list_nama_2} --> tidak ikut berubah.\n')


# Merubah isi list var kedua
print('Merubah isi var kedua'.center(50,'='))

print(f'Data nama 1 = {list_nama_1} --> tidak ikut berubah.')

list_nama_2[2] = 'Ucup'
print(f'Data nama 2 = {list_nama_2} --> Index ke-2 diubah jadi "Ucup".')
