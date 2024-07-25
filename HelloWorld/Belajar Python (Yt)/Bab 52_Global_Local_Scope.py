# GLOBAL & LOCAL SCOPE

import os
os.system('cls')



# GLOBAL SCOPE
# Variabel Global dibuat sebelum pembuatan rumus fungsinya


# Contoh 1:  --> Var Global di dalam fungsi
nama_global = 'sakura'     # --> ini adalah variabel global. Bisa dipanggil pada bentuk2/ format yang ada titik 2 nya.

def fungsi():
    print(f'Fungsi menampilkan nama: {nama_global}')
fungsi()


# Contoh 2:  --> Var Global di dalam loop
keterangan = 'You deserve better!'

for i in range(0,5):
    print(f'Loop {i} --> {keterangan}')


# Contoh 3:  --> Var Global di percabangan
if True:
    print(f'format percabangan(if): menampilkan {nama_global}')


# Contoh 4:  Variabel Global dibuat setelah pembuatan rumus fungsi nya.
def fungsi_nama():
    print(f'Nama Panjang: {nama_panjang}')

nama_panjang = 'Ucok Baba'
fungsi_nama()



# LOCAL SCOPE
# var lokal yang hanya hidup di dalam rumus saja

def fungsi():
    nama_local = 'Niman Suniman' # ini variabel lokal  --> ga bisa diakses di luar rumus fungsi

fungsi()  # ga akan muncul jika karena di luar rumus fungsi
# print(nama_local)   --> jika uncomment, var 'nama_local' akan muncul garis kuning dgn ket: "is not defined"



# MERUBAH ISI VARIABEL GLOBAL

# Contoh 1:  --> kata GPT, cara ini (return fungsi) lebih disarankan karena mudah & jelas & tidak ribet dan lain2
# bisa untuk semua jenis format yang ada titik 2 nya
angka = 0

def fungsi_ubah_angka(angka_baru):
    angka = angka_baru
    return angka

print(f'Angka sebelum diubah = {angka}')
angka_berubah = fungsi_ubah_angka(10)    # --> dibuat variabel baru untuk menerapkan si return
print(f'Angka setelah diubah = {angka_berubah}\n')


# Contoh 2:
nama = 'ucup'

def fungsi_nama(nama_baru):
    nama = nama_baru
    return nama   # harus direturn

print(f'Nama setelah diubah = {fungsi_nama("sakura")}\n')



# Atau Dgn Memanggil 'global' / Meminta Akses   --> hanya bisa dipake di bentuk fungsi saja
# Contoh 1:
def fungsi_ubah_angka(angka_baru):
    global angka   # --> minta akses
    angka = angka_baru

print(f'Angka sebelum berubah = {angka}')
fungsi_ubah_angka(10)
print(f'Angka setelah berubah = {angka}')  # --> pake variabel yg sama dgn variabel global awal, tapi isinya dieksekusi ke rumus fungsi dulu


# Contoh 2:
angka = 0
nama = 'ucup'

def fungsi_nama_angka(nama_baru, angka_baru):
    global nama
    global angka
    nama = nama_baru
    angka = angka_baru

print(f'Nama lama: {nama}, nomor angka lama: {angka}')
fungsi_nama_angka('Jiten',99)
print(f'Nama baru: {nama}, nomor angka baru: {angka}')


# Pada bentuk bukan fungsi, bisa TIDAK MEMAKAI pernyataan 'GLOBAL'
# Contoh 3:  --> bisa diprint walau tidak direturn
angka = 0

for i in range(0,5):
    angka += i
    angka_lain = 0

print(angka)
print(angka_lain)


# Contoh 4:   
if True:
    angka = 10
    angka_lain = 50

print(angka)
print(angka_lain)








