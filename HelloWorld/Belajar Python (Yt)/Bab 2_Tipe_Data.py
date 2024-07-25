
print('=============== TIPE DATA ================')
# a = 10, artinya a adalah variable dengan nilai 10

# tipe data: Angka tidak ada koma / bil bulat (Integer)
from ctypes import c_double
data_integer = 12
print(f'Data = {data_integer}, bertipe: {type(data_integer)}')


# tipe data: Angka dgn koma / desimal (Float)
data_float = 3.4
print(f'Data = {data_float}, bertipe: {type(data_float)}')


# tipe data: kumpulan karakter / kata (string)
data_string = 'jaehyun'
print(f'Data = {data_string}, bertipe: {type(data_string)}')


# tipe data: biner yaitu True/False (Boolean)
data_bool = False
print(f'Data = {data_bool}, bertipe: {type(data_bool)}')

print()


# tipe data khusus:

# Bilangan kompleks
print('Bilangan kompleks = 5 + 7i')
"Angka 5 = bil riil, sedangkan 7i = bil imajiner. Huruf 'i' bisa ganti jadi huruf apa aja"
print('maka')
data_complex = complex(5, 7)
print(f'Data = {data_complex}, bertipe: {type(data_complex)}')

print()

# Bahasa C
data_c_double = c_double(100.56)
print(f'Data  = {data_c_double}, bertipe: {type(data_c_double)}')

print()