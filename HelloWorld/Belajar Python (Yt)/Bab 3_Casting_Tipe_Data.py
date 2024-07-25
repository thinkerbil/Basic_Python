print('=================== MENGUBAH TIPE DATA ===================')
# CASTING DATA = mengubah satu tipe data ke tipe data yang lain
# tipe data: int (integer), float, str (string), bool(boolean)


# INTEGER
print('========== INTEGER ==========')
data         = 9
print(f'data = {data}, tipe: {type(data)}')

data_float   = float(data)
data_str     = str(data)
data_bool    = bool(data)
print(f'float = {data_float}, tipe: {type(data_float)}')
print(f'str = {data_str}, tipe: {type(data_str)}')
print(f'bool = {data_bool}, tipe: {type(data_bool)}')
# boolean: Angkanya bernilai (+) atau (-) akan TRUE. Kalau nol (0) akan FALSE

print()

# FLOAT
print('========== FLOAT ==========')
data   = 4.3
print(f'Data = {data}, tipe: {type(data)}')

data_int     = int(data)
data_str     = str(data)
data_bool    = bool(data)
print(f'int = {data_int}, tipe: {type(data_int)}')
print(f'str = {data_str}, tipe: {type(data_str)}')
print(f'bool = {data_bool}, tipe: {type(data_bool)}')

print()

# BOOLEAN
print('========== BOOLEAN ==========')
data    = False
print(f'Data = {data}, tipe {type(data)}')

data_int     = int(data)
data_float   = float(data)
data_str     = str(data)
print(f'int = {data_int}, tipe: {type(data_int)}')
print(f'float = {data_float}, tipe: {type(data_float)}')
print(f'str = {data_str}, tipe: {type(data_str)}')

print()

# STRING
print("========== STRING ==========")
data     = "0999.40092"
print(f'data = {data}, tipe: {type(data)}')

data_float   = float(data)
data_int     = int(data_float)
data_bool    = bool(data)
print(f'int = {data_int}, tipe: {type(data_int)}')
print(f'float = {data_float}, tipe: {type(data_float)}')
print(f'bool = {data_bool}, tipe: {type(data_bool)}')

# Jika isi dari variabel data str = "karakter" -> diubah ke tipe data lain -> error.
# Jika isi dari variabel data str = "angka" -> diubah ke tipe data lain -> bekerja.