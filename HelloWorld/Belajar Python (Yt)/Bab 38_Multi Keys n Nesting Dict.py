# MULTI KEYS & NESTING LIST


# MULTI KEYS
print('NESTING DICTIONARY'.center(40,'='))

import datetime
data_mahasiswa_1 = {
    'Nama'         : 'Sakura Haruka',
    'NIM'          : 19023001,
    'SKS lulus'    : 130,
    'Tahun lulus'  : '2025',
    'Tanggal lahir': datetime.datetime(2002,2,28)
}

print(data_mahasiswa_1)

print()

for key,value in data_mahasiswa_1.items():
    print(f'{key}: {value}\n')



# NESTING DICTIONARY
# --> akan dibuat dictionary di dalam dictionary
print('NESTING DICTIONARY'.center(40,'='))

data_mahasiswa_1 = {
    'Nama'         : 'Sakura Haruka',
    'NIM'          : 19023001,
    'SKS lulus'    : 140,
    'Tahun lulus'  : '2025',
    'Beasiswa'     : False,
    'Tanggal lahir': datetime.datetime(2002,2,28)
}

data_mahasiswa_2 = {
    'Nama'         : 'Ucok Surucok',
    'NIM'          : 19023002,
    'SKS lulus'    : 130,
    'Tahun lulus'  : '2025',
    'Beasiswa'     : True,
    'Tanggal lahir': datetime.datetime(2002,6,6)
}

data_mahasiswa_3 = {
    'Nama'         : 'Spongebob Squarepants',
    'NIM'          : 19023003,
    'SKS lulus'    : 100,
    'Tahun lulus'  : '2028',
    'Beasiswa'     : False,
    'Tanggal lahir': datetime.datetime(1997,1,31)
}

data_mahasiswa = {
    'Key 1': data_mahasiswa_1,
    'Key 2': data_mahasiswa_2,
    'Key 3': data_mahasiswa_3
}

print(data_mahasiswa)

print()


# Iterasi Value Data Nesting Dict
print('ITERASI VALUE DATA NESTING DICT'.center(50,'='))

values = data_mahasiswa.values()
print(values)

print()


# Mengeluarkan Value Nesting Dict
print('MENGELUARKAN VALUE DATA NESTING DICT'.center(50,'='))
for value in data_mahasiswa.values():
    print(value)

print()


#  Mengeluarkan Item Data Nesting Dict menjadi bentuk loop pada nesting dict
print('MENGELUARKAN ITEM DATA NESTING LIST MJD LOOPING'.center(50,'='))
for key,value in data_mahasiswa.items():
    print(f'{key} : {value}')

print(f"\n"*2)



# Contoh Bikin Database Dengan Dictionary
print(f'{"Contoh DataBase".center(40,"=")}\n')
data_mahasiswa = {
    'MHS001': data_mahasiswa_1,
    'MHS002': data_mahasiswa_2,
    'MHS003': data_mahasiswa_3
}

print(f'{"KEY":^8} {"NAMA":^25} {"NIM":^15} {"SKS":^6} {"BEASISWA":^10} {"LAHIR":^10}') # Membuat Baris Pertama Database
print('-'*80)


for mahasiswa in data_mahasiswa.keys():
    # output dari: print(mahasiswa)  --> adalah key dari dictionary data_mahasiswa. Output var KEY di bawah sama seperti print(mahasiswa)
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['Nama'] # Ingin mengambil key 'Nama' dari dict di dalam nested dict
    NIM = data_mahasiswa[KEY]['NIM']
    SKS = data_mahasiswa[KEY]['SKS lulus']
    BEASISWA = data_mahasiswa[KEY]['Beasiswa']
    LAHIR = data_mahasiswa[KEY]['Tanggal lahir'].strftime("%x")
    
    print(f'{KEY:^8} {NAMA:<25} {NIM:^15} {SKS:^6} {BEASISWA:^10} {LAHIR:^10}')

print()
    








