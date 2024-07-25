# *args
# fungsinya: memudahkan def argumen fungsi apabila argumennya banyak
# tipe args : tuple --> (....)

import os
os.system('cls')

# Contoh Tanpa *args
# Contoh 1:
def data_diri(nama,tinggi,berat):
    print(f'Si {nama} punya tinggi {tinggi}cm dan beratnya {berat}kg')

data_diri('Sakura',170,54)

# Contoh 2:
def data_diri(data_list):
    data_list_copy = data_list.copy()
    nama = data_list_copy[0]
    tinggi = data_list_copy[1]
    berat = data_list_copy[2]
    print(f'Si {nama} punya tinggi {tinggi}cm dan berat {berat}kg')

data_diri(['Ucok',160,55]) # harus dibuat menjadi data list, kalau tidak akan menjadi error output nya


# Sehingga, agar mudah dan tidak pusing dan secara otomatis program yang akan menyesuaikan, maka pakai *args
# Contoh 1:
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'Si {nama} punya tinggi {tinggi}cm dan berat {berat}kg')

fungsi('Umemiya',177,61)


# contoh 2:
def fungsi(*data):
    hasil = 0
    for angka in data:
        hasil += angka
    return hasil

print(f'Hasil = {fungsi(1,2,3,4,5,6,7,8,9)}')
print(f'Hasil = {fungsi(10,10,20)}')



    










