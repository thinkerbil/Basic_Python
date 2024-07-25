# LOOPING LIST

# For Loop --> konsep nya setiap satu putaran, variabel (ex: angka) keluar / mengeksekusi satu data pada list
print('FOR LOOP'.center(30,'='))
kumpulan_angka = [4,3,2,5,6,7]

for angka in kumpulan_angka:
    print(f'Angka = {angka}')
          
print()

peserta = ['sakura','ujang','suo']
for nama in peserta:
    print(f'Nama peserta = {nama}')

print()


# For Loop dengan Range
print('FOR LOOP dgn RANGE'.center(30,'='))
kumpulan_angka = [9,8,5,4,3,2]

panjang_baris = len(kumpulan_angka)

for i in range(panjang_baris):
    print(f'Angka = {kumpulan_angka[i]}') # i nya seperti index

print()


# While Loop
print('WHILE LOOP'.center(30,'='))
kumpulan_angka = [4,3,2,5,6,7]
panjang_baris = len(kumpulan_angka)

i = 0

while i < panjang_baris:
    print(f'Angka = {kumpulan_angka[i]}') # i nya seperti index
    i += 1

print()


# LIST COMPREHENSION
print('LIST COMPREHENSION'.center(30,'='))
angka = [1,2,3,4,5]

[print(i) for i in angka]
print()

[print(f'Angka = {i}') for i in angka]
print()

[print(f'Angka = {i**2}') for i in angka] # i nya dioperasi matematika

# Membuat List baru dari list angka
angka_kuadrat = [i**2 for i in angka]
print(f'Angka = {angka_kuadrat}')
print()


# ENUMERATE
print('ENUMERATE'.center(30,'='))
list_data = [1,2,3,'sakura','suo']

for index,data in enumerate(list_data):
    print(f'Index: {index} \tData: {data}')

