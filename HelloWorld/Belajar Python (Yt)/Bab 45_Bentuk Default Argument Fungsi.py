# DEFAULT FUNGSI

import os
os.system('cls')

# Bentuk fungsi:
# def fungsi(argument):
        # isi fungsi

# def fungsi(argument = nilai default nya):
        # isi fungsi
# mempermudah penulisan



# Contoh 1 --> argumen dgn variabel saja (value variabelnya ditulis di luar fungsi)
def panggil(nama):
    print(f'Halo {nama}')

panggil('Sakura')
panggil('Umemiya')
panggil('Togame')


# Contoh 2 --> argumen dgn variabel beserta value
def kalimat(kata_kata = 'Sip keren'):
    print(kata_kata)

kalimat()


# Contoh 3 --> argument dgn 2 variabel
def menyapa(nama,pesan_teks):
    print(f'Woi {nama}, {pesan_teks}')

menyapa('Sakura','Gelut teros lu')


# Contoh 4 --> argument dgn 2 variabel yang salah satunya ber-value (hanya variabel akhir yang bisa punya value)
def nyapa(nama,pesan = 'sehat-sehat orang baik'):
    print(f'{nama}, {pesan}')

nyapa('Sakura Haruka') # panggil nama aja, pesan ga usah karena udah dibuat di fungsi


# Contoh 5 --> Mengakses variabel pada definisi argument fungsi di pemanggilan fungsi
def hitung(angka_a, pangkat_a):
    hasil = angka_a**pangkat_a
    return hasil

print(hitung(5,2)) # cara biasa

print(hitung(angka_a = 2, pangkat_a = 5)) # akses variabel fungsi


# Contoh 6 --> value variabel pada definisi argument fungsi berbeda dgn value variabel pada pemanggilan argument fungsi
def menghitung(angka_b, pangkat_b = 2):
    jawaban = angka_b**pangkat_b
    return jawaban

print(menghitung(angka_b=2, pangkat_b=7))


# Contoh 7 --> Mengubah salah satu value argument
def calculate(angka1=1, angka2=2, angka3=3, angka4=4):
    y = angka1 + angka2 + angka3 + angka4
    return y

print(calculate()) # menghitung dgn angka2 sesuai def fungsi nya
print(calculate(angka3 = 4)) # merubah value angka3 pada def argumen fungsi