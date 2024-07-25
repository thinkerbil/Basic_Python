# FUNGSI DENGAN ARGUMENT

# Argument (atau Input) adalah dalamnya dalam kurung fungsi   -->  def fungsi(argument)
# gunanya, bisa buat merubah2 output

import os
os.system('cls')


# Contoh 1: Argument tipe String
def menyapa(nama):
    print(f'Selamat datang di Isekai wahai {nama}')

menyapa('Sakura.\n')



# Contoh 2: Argument tipe Angka
def penjumlahan(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')

penjumlahan(5,7)
penjumlahan(10.2,115)
penjumlahan(42,24)

print()



# Contoh 3: Argument tipe list
def memanggil(list_nama):
    # misal: tidak di-copy. Apabila:
    # list_nama[1] = 'Ucup'     # --> data 'nama_nama_orang' ikut berubah
    data_nama = list_nama.copy()  # karena 'list_nama' dpt dari var 'nama_nama_orang' --> pake format copy utk menghindari JIKA terjadi perubahan data
    for nama in data_nama:
        print(f'Selamat datang juga untuk {nama} di Isekai.')

nama_nama_orang = ['Suo','Togame','Umemiya','Isayama']   # Ini adalah data tambahan di luar fungsi

memanggil(nama_nama_orang)   # var yang masuk ke argument, berubah menjadi 'list_nama' (akan dieksekusi di baris def)


