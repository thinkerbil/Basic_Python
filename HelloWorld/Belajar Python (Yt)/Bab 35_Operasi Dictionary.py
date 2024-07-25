# OPERASI PADA DICTIONARY

# Operator untuk memanggil key & values di dictionary


data_dict = {
    'cp':'ucup surucup',
    'tg':'otong surotong',
    'dg':'dudung surudung',
    'skr':'sakura haruka',
    'sp':'asep sukasep',
    'rd':'rudi surudi'
}
print(f'Data dictionary = {data_dict}') # Output: iterasi menyamping ('key':'value')


# METHODE-METHOD

# 1. Menghitung Panjang Dictionary   -->   len(var)
PANJANG_DICT = len(data_dict) # variabel baru harus kapital semua (khusus untuk dictionary)
print(f'Panjang dictionary = {PANJANG_DICT}\n')


# 2. Mengecek Suatu KEY Apakah ada/tidak Pada Data Dictionary
# Cara Biasa
KEY = 'skr'
CHECK_KEY = KEY in data_dict
print(f'Apakah key "{KEY}" ada di data dictionary? {CHECK_KEY}')

KEY = 'umm'
CHECK_KEY = KEY in data_dict
print(f'Apakah key "{KEY}" ada di data dictionary? {CHECK_KEY}\n')



# 3. Mengakses VALUE / Memanggil suatu KEY

# Cara Biasa --> var["key"]
print(f'Panggil key "skr": {data_dict["skr"]}')
print(f'Panggil key "tg": {data_dict["tg"]}')
# print(f'Panggil key "cy": {data_dict["cy"]}')

# kalau manggil suatu key tapi key nya ga ada di data dictionary -> akan terjadi error
# solusi:


# Mengakses VALUE Pake Method get   -->   var.get("key")
print(f'Panggil key "rd": {data_dict.get("rd")}')
print(f'Panggil key "sp": {data_dict.get("sp")}')
print(f'Panggil key "cy": {data_dict.get("cy")}') # Kalau pake get, keluarnya "None" karena key 'cy' tidak ada di data dict


# Mengganti output "None" jika key tidak ada di data dict   -->   var.get("cy","kalimat lain jika key tidak ada di data dict.")
print(f'Panggil key "cy": {data_dict.get("cy","Key tidak ditemukan")}\n')


# 4. Mengubah & Meng-Update Data Dictionary

# Cara Biasa
data_dict['tg'] = "tunggu kiris"
print(f'Perubahan Data Dict: {data_dict}\n')

data_dict['cy'] = 'ucuy surucuy'
print(f'Data Dict bertambah: {data_dict}\n')


# Cara Merubah Data & Otomatis Nambah Jika Data ga ada   -->  var.update({"key": "value"})

# Merubah kembali value dari 'tg'
data_dict.update({"tg":"otong surotong"})
print(f'Data dict baru saat value "tg" diubah kembali: {data_dict}\n')

# Menambah Data secara otomatis jika ga ada di data dict
data_dict.update({"umm": "umemiya mamamiya"})
print(f'Data dict baru penambahan item: {data_dict}\n')



# 5. Hapus/Delate Item Data DIctionary   -->   del var["key"]
del data_dict["umm"]
print(f'Data dict paling baru: {data_dict}\n')

























