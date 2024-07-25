# CONTOH DICTIONARY ke-2


# Membuat Database dgn menggunakan Dictionary Kosong
# Menggunakan Method     -->     dict.fromkeys(var)


# Membuat Database Dari Input User
# Membuat template dictionary nya dahulu
import datetime

import os       # untuk menghapus tulisan2 atas nya output (yang seperti lokasi file)



data_mahasiswa_template = {
    'Nama': 'nama',
    'NIM': '00000000',
    'sks lulus': 0,
    'Beasiswa': 'beasiswa',
    'Lahir': datetime.datetime(1111,1,11)
}

data_mahasiswa = {} 

os.system("cls") # untuk menghapus tulisan2 atas nya output (yang seperti lokasi file)


print(f'{"SELAMAT DATANG".center(40," ")}\n{"SILAHKAN INPUT DATA ANDA".center(40,"-")}')

# memanggil keys template beserta isinya
mahasiswa = dict.fromkeys(data_mahasiswa_template.keys()) 


# ingin mengisi template sesuai keys 'Nama', 'NIM', 'sks lulus', 'lahir', maka dilakukan pengubahan value:
mahasiswa['Nama'] = input('Masukkan nama Anda: ') 

mahasiswa['NIM'] = input('Masukkan NIM Anda: ')

mahasiswa['sks lulus'] = int(input('Masukkan SKS lulus Anda: '))

mahasiswa['Beasiswa'] = bool(input('Masukkan keterangan beasiswa Anda: '))

TAHUN_LAHIR = int(input('Masukkan tahun lahir Anda (YYYY): '))
BULAN_LAHIR = int(input('Masukkan bulan lahir Anda (1-12): '))
TANGGAL_LAHIR = int(input('Masukkan tanggal lahir Anda (1-31): '))
mahasiswa['Lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)



print('\n')

# Dibuat Database
print(f'{"NAMA":^15} {"NIM":^12} {"SKS":^8} {"BEASISWA":^11} {"LAHIR":^10}')
print('-'*65)

for info_data in mahasiswa.keys():
    # KEY = info_data
    # print(KEY)
    NAMA = mahasiswa['Nama']
    NIM = mahasiswa['NIM']
    SKS_LULUS = mahasiswa['sks lulus']
    BEASISWA = mahasiswa['Beasiswa']
    LAHIR = mahasiswa['Lahir'].strftime("%x")
    
print(f'{NAMA:^15} {NIM:^12} {SKS_LULUS:^8} {BEASISWA:^11} {LAHIR:^11}\n')





