# FUNGSI DENGAN RETURN / PENGEMBALIAN

import os
os.system('cls')

# ibarat f(x) --> argument sbg 'x' nya. dan f = nama fungsi nya
# di dalam def, kita buat seperti:
# def f(x):
        # f(x) = buat rumus fungsinya
        # return f(x) --> kembalikan hasil dari f(x) ke f(x) itu sendiri, 
        # dgn tujuan apabila kita mendapat soal variasi, seperti misal: f(5) --> 5 = x --> masukkan f(5) ke f(x)
# Note: kita tidak bisa buat nama fungsinya seperti: 'f(x)' atau 'fungsi'


# Contoh 1
def kuadrat(x):
    hasil = x**2
    return hasil

y = kuadrat(7)
print(f'7 kuadrat = {y}')

print(f'11 kuadrat = {kuadrat(11)}')

a = 12 + kuadrat(5)
print(f'12 + 5 kuadrat = {a}')

print(f'3 + 5 kuadrat = {3 + kuadrat(5)}')



# Contoh 2 --> Argumen diisi 2 angka
def penjumlahan(angka_1,angka_2):
    return angka_1 + angka_2

z = penjumlahan(30,5)
print(f'30 + 5 = {z}')

print(f'12 + 3 = {penjumlahan(12,3)}')



# Contoh 3 --> Fungsi nya / rumus nya banyak
def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    pangkat = angka_1**angka_2
    return tambah,kurang,kali,bagi,pangkat

tambah,kurang,kali,bagi,pangkat = operasi_matematika(10,2)
print(f'''hasil pertambahan = {tambah}
hasil pengurangan = {kurang}
hasil perkalian = {kali}
hasil pembagian = {bagi}
hasil pangkat = {pangkat}
''')



    