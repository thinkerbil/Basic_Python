# DEEP COPY

# Deep copy = copy untuk nested list (list di dalam list)


x = [1,2,3]
y = [5,6,7]
nested_list = [x,y]
print(f'List x = {x}')
print(f'List y = {y}')
print(f'Nested List = {nested_list}')

# Copy biasa
nested_list_copy = nested_list.copy()
print(f'Nested List copy = {nested_list_copy}\n')

# Address masing-masing list
print(f'Address Nested List asli           = {hex(id(nested_list))}')
print(f'Adress Nested List copy            = {hex(id(nested_list_copy))}')
print('--> Address Nested List asli dgn Nested list copy beda.\n')

# Cek adress member Nested List Asli & Copy
print('=== Cek Address Index ke-0 Nested List Asli dgn Nested List Copy ===')
print(f'Adress index ke-0 Nested List Asli = {hex(id(nested_list[0]))}')
print(f'Adress index ke-0 Nested List Copy = {hex(id(nested_list_copy[0]))}')
print('--> Address index ke-0 Nested List asli dgn Nested list copy SAMA.\n')


print('Simpulan : Jika meng-copy / menduplikat Nested List --> yg terduplikat cuma list luar nya aja. LIST DALAM NYA TIDAK TERDUPLIKAT.\n')


print('Sehingga, apabila merubah isi list di dalam nested list') 
# Merubah isi Nested List
# Merubah index ke-0 list pertama pada nested list menjadi 4
print(f'Nested List asli lama   = {nested_list}')
print(f'Nested List copy        = {nested_list_copy}\n')

print('(merubah indeks ke-0 list pertama nested list asli)')
nested_list[0][0] = 4
print(f'Nested List asli baru   = {nested_list}')
print(f'Nested List copy        = {nested_list_copy}')
print('--> Perubahan isi list di dalam nested list asli juga dialami oleh isi list di dalam nested list copy.')


print('''
Simpulan : Jika meng-copy / menduplikat Nested List --> yg terduplikat cuma list luar nya aja. LIST DALAM NYA TIDAK TERDUPLIKAT.
Solusi   : duplikat nested list BUKAN pakai COPY. Tapi PAKAI DEEPCOPY.
''')


# DEEP COPY
# cara: harus import deepcopy dulu
# method: deepcopy(var)
print('DEEPCOPY'.center(40,'='))

x = [1,2,3]
y = [5,6,7]
nested_list = [x,y]

from copy import deepcopy
nested_list_deepcopy = deepcopy(nested_list)

print(f'Nested List          = {nested_list}')
print(f'Nested List deepcopy = {nested_list_deepcopy}\n')

# Cek address
print(f'Adsress Nested List asli            = {hex(id(nested_list))}')
print(f'Address nested list deepcopy        = {hex(id(nested_list_deepcopy))}')
print(f'Adsress member nested list asli     = {hex(id(nested_list[0])), hex(id(nested_list[1]))}')
print(f'Adsress member nested list deepcopy = {hex(id(nested_list_deepcopy[0])), hex(id(nested_list_deepcopy[1]))}')
print('--> ADDRESS MEMBER Nested List asli dgn Nested List deepcopy BERBEDA.\n')


print('Contoh: Merubah isi list di dalam nested list') 
# Merubah isi Nested List
# Merubah index ke-0 list pertama pada nested list menjadi 4
print(f'Nested List asli lama   = {nested_list}')
print(f'Nested List deepcopy        = {nested_list_deepcopy}\n')

print('(merubah indeks ke-0 list pertama nested list asli)')
nested_list[0][0] = 4
print(f'Nested List asli baru   = {nested_list}')
print(f'Nested List deepcopy        = {nested_list_deepcopy}')
print('--> Perubahan isi list di dalam nested list asli tidak dialami oleh isi list di dalam nested list deepcopy.')


