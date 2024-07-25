# FUNGSI LAMBDA / LAMBDA FUNCTION
# Mempermudah penulisan kode program

import os
os.system('cls')

# Contoh Format Fungsi biasa
def kuadrat(angka):
    return angka**2

print(f'Hasil Fungsi Biasa kuadrat dari 5 = {kuadrat(5)}')


# CONTOH PENULISAN DENGAN FUNGSI LAMBDA
# Format:
# var_output = lambda argumen: expression/isi fungsi    -->   pemanggilannya: var_output(argumen)

# Contoh 1: Argumennya 1
kuadrat = lambda angka: angka**2 # argumennya adalah "angka"
print(f'Hasil Fungsi Lambda kuadrat dari 4 = {kuadrat(4)}')

# Contoh 2: Argumennya 2
pangkat = lambda number,power : number**power
print(f'3 pangkat 6 adalah = {pangkat(3,6)}\n')



# KEGUNAAN LAMBDA FUNCTION

# 1. Sorting / Mengurutkan Data List

# Cara Biasa:
# --> Mengurutkan berdasarkan Abjad
data_list = ['Ucok','Bonat','Toeing']
data_list.sort()
print(f'Sorted List dgn Abjad = {data_list}')

# --> Mengurutkan berdasarkan Panjang / Banyaknya Huruf
data_list.sort(key = len)
print(f'Sorted List dgn panjang huruf = {data_list}')

# --> contoh pakai fungsi
data_list = ['Ucok','Bonat','Toeing']
def panjang_nama(nama):
    return len(nama)

data_list.sort(key = panjang_nama)
print(f'Sorted List dgn panjang huruf pakai fungsi = {data_list}')


# Cara Lambda:
# --> Sorted berdasarkan huruf
data_list = ['Ucok','Bonat','Toeing']
data_list.sort(key = lambda nama: nama)
print(f'Sorted List dgn Abjad pakai Lambda = {data_list}')

# --> Sorted berdasarkan panjang nama
data_list = ['Ucok','Bonat','Toeing']
data_list.sort(key = lambda nama: len(nama)) # 'nama' as argumen (dirujuk ke isi dari List var data_list)
print(f'Sorted List dgn panjang huruf pakai Lambda = {data_list}\n')



# 2. Filter dgn Lambda  --> filter(lambda argument: expression, var_original)
# Contoh dgn Data List:
list_angka = [1,2,3,4,5,6,7,8,9,10]
filter_angka_kurang_dari_lima = list(filter(lambda x: x<5, list_angka)) # dari data list angka, akan dipilih angka2 (x) yang kurang dari 5
print(f'List Angka: {list_angka}')
print(f'Filter angka yang kurang dari 5 = {filter_angka_kurang_dari_lima}')

# Contoh filter angka genap:
list_angka = [1,2,3,4,5,6,7,8,9,10]
filter_angka_genap = list(filter(lambda x:(x%2 == 0), list_angka))
print(f'Filter angka genap = {filter_angka_genap}')

# Contoh filter angka ganjil:
list_angka = [1,2,3,4,5,6,7,8,9,10]
filter_angka_ganjil = list(filter(lambda x:(x%2 != 0), list_angka))
print(f'Filter angka ganjil = {filter_angka_ganjil}')

# Contoh filter angka kelipatan 3:
list_angka = [1,2,3,4,5,6,7,8,9,10]
filter_angka_kelipatan_3 = list(filter(lambda x:(x%3 == 0), list_angka))
print(f'Filter angka kelipatan 3 = {filter_angka_kelipatan_3}\n')



# ANONYMOUS FUNCTION (masih ada hubungan dgn lambda)
# nama lain: Currying

# Contoh cara biasa:
def perpangkatan(angka,n): # n = pangkat
    hasil = angka**n
    return hasil

print(f'Hasil dari 5 pangkat 2 = {perpangkatan(5,2)}')

# Contoh cara 
def pangkat(n):
    return lambda angka: angka**n

input_angka = pangkat(4) # mengeksekusi / membuat fungsi untuk pangkatnya dulu
print(f'Hasil dari 5 pangkat 4 = {input_angka(5)}') # si input angka diisi angka 5







