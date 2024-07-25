# LATIHAN FUNGSI

# membuat program dgn fungsi dan while loop (menjadi lebih mudah)

import os

# CARA RIBET
# while True:
#     # membuat Header Program
#     os.system('cls')
#     print(f'{"PROGRAM MENGHITUNG LUAS":^40}')
#     print(f'{"DAN KELILING PERSEGI PANJANG":^40}')
#     print(f"{'-'*40:40}")

#     # Mengambil input user untuk angka satuannya
#     LEBAR = int(input('Masukkan angka untuk lebar: '))
#     PANJANG = int(input('Masukkan angka untuk panjang: ')) # variabel huruf besar (konstanta) => value diharapkan tidak berubah saat di-run

#     # Program Menghitung Luas
#     LUAS = PANJANG * LEBAR
#     KELILING = 2 * (PANJANG + LEBAR)

#     # Menampilkan Hasilnya
#     print(f'Hasil perhitungan untuk LUAS: {LUAS}')
#     print(f'Hasil perhitungan untuk KELILING: {KELILING}')
    
#     # Menanyakan program lanjut atau tidak
#     lanjut = input('Apakah lanjut (yes/no)? ')
#     if lanjut == 'no':
#         break

# Membuat program menjadi menghitung terus / meminta input terus --> Pakai looping (lebih tepatnya: WHILE LOOP)
# Kalau dilihat, pembuatan kode nya agak ribet




# CARA KEREN: PAKAI FUNGSI (Pakai while loop juga sbg pemanggilan fungsinya)
# Membuat Header Program pakai Fungsi
def header():
    os.system('cls')
    print(f'{"PROGRAM MENGHITUNG LUAS":^40}')
    print(f'{"DAN KELILING PERSEGI PANJANG":^40}')
    print(f"{'-'*40:40}")

def input_user():
    LEBAR = int(input('Masukkan angka untuk lebar: '))
    PANJANG = int(input('Masukkan angka untuk panjang: '))
    return LEBAR, PANJANG

def hitung_luas(PANJANG,LEBAR):
    return PANJANG * LEBAR

def hitung_keliling(PANJANG,LEBAR):
    return 2 * (PANJANG + LEBAR)


# Program Utamanya
while True:
    # panggil fungsi header
    header()

    # panggil fungsi input user
    LEBAR,PANJANG = input_user()
    
    # apabila hanya ingin menghitung salah satu saja (Luas saja / Keliling saja)
    hitung_luas_atau_keliling = input('Hitung Luas/Keliling (l/k/lk)? ')

    # panggil program menghitung luas
    LUAS = hitung_luas(PANJANG,LEBAR)

    # panggil program menghitung keliling
    KELILING = hitung_keliling(PANJANG,LEBAR)

    # apabila hanya ingin menghitung salah satu saja (Luas saja / Keliling saja)
    if hitung_luas_atau_keliling == 'l':
        print(f'Hasil perhitungan untuk LUAS: {LUAS}')
        
    elif hitung_luas_atau_keliling == 'k':
        print(f'Hasil perhitungan untuk KELILING: {KELILING}')
    
    else:
        print(f'Hasil perhitungan untuk LUAS: {LUAS}')
        print(f'Hasil perhitungan untuk KELILING: {KELILING}')

    # menampilkan hasil program perhitungan
    # print(f'Hasil perhitungan untuk LUAS: {LUAS}')
    # print(f'Hasil perhitungan untuk KELILING: {KELILING}')

    lanjut_ga = input('\nApakah mau lanjut (yes/no)? ')
    if lanjut_ga == 'no':
        break

print(f"{' Keluar dari program '.center(30,'-')}")





