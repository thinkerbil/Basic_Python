# LIST

# 1. List untuk Data Integer (Angka)
print('LIST ANGKA'.center(20,'='))
list_angka_1 = [1,2,3,4,5]
list_angka_2 = [2,4,6,8,10]
list_angka_3 = [1,5,3,8,6,9]
print(f'''
List angka pertama = {list_angka_1}
List angka kedua   = {list_angka_2}
List angka ketiga  = {list_angka_3}
\n''')

# 2. List untuk Data String
print('LIST STRING'.center(20,'='))
list_string_1 = ['Budi','Sakura','Ucok']
list_string_2 = ['Eko','Makan','Apel']
print(f'''
List string pertama = {list_string_1}
List string kedua   = {list_string_2}
\n''')

# 3. List untuk Data Boolean
print('LIST Boolean'.center(20,'='))
list_boolean_1 = [True,False,True,True]
list_boolean_2 = [False,False,True,True]
print(f'''
List boolean pertama = {list_boolean_1}
List boolean kedua   = {list_boolean_2}
\n''')


# 3. List untuk Data Campuran
print('LIST Campuran'.center(20,'='))
list_campuran_1 = ['Budi',17,'Forger',25,'Yor',22]
list_campuran_2 = [23,45,'Loid', 'Anya', True, False]
print(f'''
List data campuran pertama = {list_campuran_1}
List data campuran kedua   = {list_campuran_2}
\n''')



# CARA ALTERNATIF MEMBUAT LIST
print('CARA ALTERNATIF MEMBUAT LIST'.center(50,'='))


# 1. Casting List
print('CASTING Data'.center(20,'='))
data_range_1 = range(0,10)
print(f'Data sebelum di-casting ke List = {data_range_1}  --> range 0--9')
print(f'Data setelah di-casting ke List = {list(data_range_1)}\n')

data_range_2 = range(0,10,2) # range(start,stop,step) --> range dari 0--9 dengan step/lompat 2 angka
print(f'Data sebelum di-casting ke List = {data_range_2}  --> range 0--9 dgn step/lompat 2 angka')
print(f'Data setelah di-casting ke List = {list(data_range_2)}\n')


# 2. List dgn menggunakan For Loop
print('FOR LOOP LIST'.center(20,'='))
list_pake_for_1 = [i for i in range(0,10)]
list_pake_for_2 = [i for i in range(0,10,2)] # range(start,stop,step)
print(f'List data pertama (ori) = {list_pake_for_1}')
print(f'List data kedua (ori)   = {list_pake_for_2}\n')


# For Loop List bisa dioperasikan
list_pake_for_3 = [i**2 for i in range(0,10)]
list_pake_for_4 = [i**2 for i in range(0,10,2)]
list_pake_for_5 = [i*2 for i in range(0,10)]
list_pake_for_6 = [i*2 for i in range(0,10,2)]
print(f'List data pertama (dipangkatin 2)= {list_pake_for_3}')
print(f'List data kedua (dipangkatin 2)  = {list_pake_for_4}')
print(f'List data pertama (dikali 2)     = {list_pake_for_5}')
print(f'List data kedua (dikali 2)       = {list_pake_for_6}\n')


# 3. List dengan menggunakan For Loop & if
print('FOR-IF LIST'.center(20,'='))
list_pake_for_if_1 = [i for i in range(0,10) if i != 5] # angka 5 menjadi tidak ada
print(f'List data range 0--9        = {list_pake_for_if_1} --> ga ada angka 5')

list_pake_for_if_2 = [i for i in range(0,10) if i%2 == 0] # membuat bilangan genap --> pakai: modulus 2 = 0
print(f'List data genap range 0--9  = {list_pake_for_if_2}')

list_pake_for_if_3 = [i for i in range(0,10) if i%2 != 0] # membuat bilangan ganjil
print(f'List data ganjil range 0--9 = {list_pake_for_if_3}\n')


# For-If List yang dioperasikan
list_pake_for_if_1 = [i for i in range(0,10) if i != 5] # angka 5 menjadi tidak ada
list_pake_for_if_2 = [i for i in range(0,10) if i%2 == 0] # membuat bilangan genap --> pakai: modulus 2 = 0
list_pake_for_if_3 = [i for i in range(0,10) if i%2 != 0] # membuat bilangan ganjil


