# COPY & POP DICTIONARY


nama_dict = {
    'cp':'ucup surucup',
    'tg':'otong surotong',
    'dg':'dudung surudung',
    'skr':'sakura haruka',
    'sp':'asep sukasep',
    'rd':'rudi surudi'
}

# Bukan Meng-copy, tapi cuma menyimpan data dengan nama berbeda (address nya tetep sama)
name_dict = nama_dict

print(f'Data dictionary asli   = {nama_dict}')
print(f'Data dictionary rename = {name_dict}\n')

print(f'Address data dict asli  : {hex(id(nama_dict))}')
print(f'Address data dict rename: {hex(id(name_dict))}\n')
#  --> Address nya sama, karena var 'name_dict' bukan mengcopy/menduplikat data dgn ruang berbeda, tetapi hanya mengganti data dgn nama yang baru



# COPY DATA   -->  var.copy()
print('COPY DATA'.center(20,'='))

nama_dict_copy = nama_dict.copy()

print(f'Data dictionary asli = {nama_dict}')
print(f'Data dictionary copy = {nama_dict_copy}\n')

print(f'Address Data dict asli: {hex(id(nama_dict))}')
print(f'Address data dict copy: {hex(id(nama_dict_copy))}\n') # Address nya udah berbeda



# POP DATA 
# Pop data = mengambil dan mengeluarkan data dari data dictionary
print('POP DATA'.center(20,'='))

# Mengambil Data berdasarkan Key (posisi mana saja)    -->    var.pop()
sakura = nama_dict.pop("skr") # Mengambil data Sakura (key: 'skr')

print(f'Data Sakura = {sakura}')
print(f'Data Nama = {nama_dict}  --> Item sakura hilang\n')


# POP ITEM
# Menagambil Data yang Terakhir aja   --> var.popitem()
data_terakhir = nama_dict.popitem()

print(f'Data terakhir = {data_terakhir}')
print(f'Data Nama = {nama_dict}  --> item terakhir hilang\n')
