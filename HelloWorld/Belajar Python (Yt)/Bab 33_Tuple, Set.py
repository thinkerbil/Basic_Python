# TUPLE DAN SET


# Review

# LIST
print('LIST'.center(20,'='))
list_angka = [2,4,6,8,10]
print(f'contoh list = {list_angka} --> kurung kotak')
print(f'''List bisa:
- punya indeks
- bisa merubah member
- bisa insert (nambah list pada posisi yang diinginkan)
- bisa append (menambah posisi di akhir)
- bisa extend (menambah list dgn list)
- bisa remove (remove data pada list posisi yg mana aja)
- bisa pop (meremove data paling akhir)
''')


# TUPLE
# Tuple = tipe data collection yang isi data nya paten --> bentuk: pake kurung bulet '()'
print('TUPLE'.center(20,'='))
data_tuple = (1,2,3,4,5)
print(f'contoh tuple = {data_tuple} --> kurung bulat')
print(f'''Tuple:
- punya indeks
- tapi ga bisa merubah member data tuple
''')


# SET
# Set = tipe data collection yang ga punya indeks --> bentuk: pake kurung kurawal '{}'
print('SET'.center(20,'='))
data_set = {3,5,7,11,13}
print(f'contoh set = {data_set} --> kurung kurawal')
print(f'''Set:
- ga punya indeks
- mirip list
- bisa melakukan operasi manipulasi lainnya seperti pada list
''')

