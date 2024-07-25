# Contoh Dictionary 3


# Membuat Database yang terus berulang

import datetime
import os # untuk menghapus tulisan2 atas nya output (yang seperti lokasi file)
# Agar Key nya masing2 data berbeda2, pakai 2 format di bawah:
import string
import random


data_mahasiswa_template = {
    'Nama': 'nama',
    'NIM': '00000000',
    'sks lulus': 0,
    'Beasiswa': 'beasiswa',
    'Lahir': datetime.datetime(1111,1,11)
}

data_mahasiswa = {}


while True:
    # os.system("clear")  --> untuk Mac (menghapus tulisan atas nya output)
    os.system("cls") # untuk menghapus tulisan2 atas nya output (yang seperti lokasi file)

    # Ketika Benar, maka masukkan data2 input di bawah
    print(f'{"SELAMAT DATANG".center(40," ")}\n{"SILAHKAN INPUT DATA ANDA".center(40,"-")}')
    mahasiswa = dict.fromkeys(data_mahasiswa_template.keys()) 
    mahasiswa['Nama'] = input('Masukkan nama Anda: ') 
    mahasiswa['NIM'] = input('Masukkan NIM Anda: ')
    mahasiswa['sks lulus'] = int(input('Masukkan SKS lulus Anda: '))
    mahasiswa['Beasiswa'] = bool(input('Masukkan keterangan beasiswa Anda: '))
    TAHUN_LAHIR = int(input('Masukkan tahun lahir Anda (YYYY): '))
    BULAN_LAHIR = int(input('Masukkan bulan lahir Anda (1-12): '))
    TANGGAL_LAHIR = int(input('Masukkan tanggal lahir Anda (1-31): '))
    mahasiswa['Lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    # Setelah sistem mendapatkan data dari user, sistem akan menyusun data2 tsb ke Dictionary kosong dgn referensinya --> Dict Template

    # data_mahasiswa = {}   --> kalau bikin ini aja, sistem hanya akan mengulang data terus menerus ke awal lagi
    # Maka, Data harus selalu di-update / otomatis menambah data
    # Tujuan dari langkah ini adalah untuk dibuat menjadi database / tabel

    KEY = ''.join((random.choice(string.ascii_uppercase)) for i in range(6))   # Agar key nya berbeda2 setiap data yang diinput (range untuk Key nya sampai 6)
    data_mahasiswa.update({KEY: mahasiswa})  # value nya adalah mahasiswa (atau data2 yang diinput)

    
    # Agar membentuk Database
    print(f'\n{"KEY":^8} {"NAMA":^15} {"NIM":^12} {"SKS":^8} {"BEASISWA":^11} {"LAHIR":^10}')
    print('-'*70)
    
    for info_data in data_mahasiswa:
        KEY = info_data
        NAMA = data_mahasiswa[KEY]['Nama']
        NIM = data_mahasiswa[KEY]['NIM']
        SKS_LULUS = data_mahasiswa[KEY]['sks lulus']
        BEASISWA = data_mahasiswa[KEY]['Beasiswa']
        LAHIR = data_mahasiswa[KEY]['Lahir'].strftime("%x")    
        
        print(f'{KEY:^8} {NAMA:^15} {NIM:^12} {SKS_LULUS:^8} {BEASISWA:^11} {LAHIR:^11}')

    print()
    finish = input('Apakah selesai input (yes/no)? ')
    if finish == 'yes':
        break

print()
print('Program selesai'.center(21,'-'))
    