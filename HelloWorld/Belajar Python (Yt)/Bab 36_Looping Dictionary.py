# LOOPING FOR DICTIONARY


nama_dict = {
    'cp':'ucup surucup',
    'tg':'otong surotong',
    'dg':'dudung surudung',
    'skr':'sakura haruka',
    'sp':'asep sukasep',
    'rd':'rudi surudi'
}

# Looping Biasa
for nama in nama_dict:
    print(f'Nama = {nama} --> yang keluar key nya.')
print()



# METHOD / OPERATOR UNTUK LOOPING

# Operator untuk mengambil item (sistem iterables)

# 1. Iterasi 1: Iterasi Key     -->    var.keys()
KEY = nama_dict.keys()
print(f'{KEY}   --> Iterasi 1 : Iterasi Key')

# Karena KEY udah dipanggil     --> bisa ngakses/manggil value  --> var.get("key")
for key in nama_dict.keys():
    print(f'Values Iterable 1 dictionary = {nama_dict.get(key)}')   # "key" nya dalam bentuk variabel


print()



# 2. Iterasi 2: Iterasi Value    -->    var.values()
value = nama_dict.values()
print(f"{value}  --> Iterasi 2: Manggil values")


# Karena VALUE udah Dipanggil    --> bisa keluarin value dalam bentuk memanjang ke bawah
for value in nama_dict.values():
    print(f'Value iterable 2 dictionary = {value}')
print()



# 3. Iterasi 3: Iterasi Item     -->   var.items()
panggil_items = nama_dict.items()
print(panggil_items)

# Item yang udah dipanggil bisa jadiin bentuk memanjang ke bawah / loop
# outputnya: tuple2 dari 'key' & 'value' dlm bentuk looping
for item in nama_dict.items():
    print(item)

print()

# Dirapihin bentuk key dgn value nya:
for key,value in nama_dict.items():
    print(f'Key : {key:6} Value : {value}')

print()