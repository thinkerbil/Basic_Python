# **kwargs
# keyword args
# args yang argumennya memakai key
# type **kwargs : dictionary

import os
os.system('cls')


# Perhatikan
def fungsi(nama,tinggi,berat):
    print(f'Si {nama} punya tinggi {tinggi} dan berat {berat}')

fungsi('Sakura',177,65) # memanggil fungsinya


# perhatikan bentuk output kwargs
def fungsi(**kwargs):
    print(kwargs)

# fungsi('Sakura',177,65)   --> kalau begini doang akan error
fungsi(nama='Sakura', tinggi= 177, berat= 65) # tidak akan error jika pakai key  --> Putput: Dictionary


# Bisa memilih data mana yang mau diambil/dikeluarkan dgn cara: panggil pake KEY nya
def fungsi(**kwargs):
    print(kwargs["nama"])
    print(kwargs["berat"])
    # atau bisa ditulis dgn cara:
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f'Si {nama} punya tinggi {tinggi} dan berat {berat}\n')

fungsi(nama = 'Ucok', tinggi = 168, berat = 48)



# Contoh lain
def math(*args,**kwargs):   # urutannya: *args dulu baru **kwargs
    output = 0
    if kwargs["operasi"] == 'Penjumlahan':
        print('Operasi Penjumlahan')
        for angka in args:
            output += angka
    elif kwargs["operasi"] == 'Perkalian':
        print('Operasi Perkalian')
        for angka in args:
            output += angka
    else:
        print('Operasi Tidak Ditemukan')
    return output

hasil = math(1,2,3,4,5,6,7,8,operasi = 'Penjumlahan')
print(f'Hasil penjumlahan = {hasil}')

hasil = math(1,2,3,4,5,6,7,8,operasi = 'Perkalian')
print(f'Hasil perkalian = {hasil}')









