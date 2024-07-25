# NESTED LIST
# List Bersarang = List di dalam list


print('Contoh Sederhana'.center(30,'='))

# Contoh 1
print('Contoh 1:')
x = [1,2]
y = [3,4]
q = [x,y] # Contoh Nested List yang berisi data2 list di atas
print(f'List X = {x}')
print(f'List Y = {y}')
print(f'List Q = {q} --> Nested List.\n')


# Contoh 2
print('Contoh 2:')
a = ['ucup','budi']
b = ['jubaedah','dedeh']
d = [a,b] # Contoh Nested List yang berisi data2 list di atas
print(f'List A = {a}')
print(f'List B = {b}')
print(f'List D = {d} --> Nested List.\n')


# Contoh 3
print('Contoh 3:')
print(f'List A = {a}')
print(f'List B = {b}')

d = [a,b,2,4]
print(f'List D = {d} --> Nested List campuran.\n')


# Contoh 4
print('Contoh 4:')
peserta_1 = ['Budi',13,'laki-laki']
peserta_2 = ['jubaedah',13,'perempuan']
peserta_3 = ['hamid',14,'laki-laki']
print(f'''data peserta 1 = {peserta_1}
data peserta 2 = {peserta_2}
data peserta 3 = {peserta_3}''')

print(f'\nData peserta = {peserta_1,peserta_2,peserta_3}\n')



# MEMANGGIL ISI DATA
print('MEMANGGIL LIST DI DALAM NESTED LIST'.center(50,'='))
x = [1,2]
y = [3,4]
print(f'List X = {x}')
print(f'List Y = {y}')

q = [x,y]
print(f'List Q = {q} --> Nested List.')

print(f'Panggil list ke-0 dari nested list = {q[0]}') # dipanggil dgn menggunakan pemanggilan dgn index
print(f'Panggil index ke-0 list ke-0 dari nested list = {q[0][0]}') 
# index yang ditulis adalah pemanggilan index untuk list di dlm nested list, lalu pemanggilan index untuk isi list
print(f'Panggil list ke-1 dari nested list = {q[1]}')
print(f'Panggil index ke-0 list ke-1 dari nested list = {q[1][0]}') 



