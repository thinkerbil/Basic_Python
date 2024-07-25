# LOOP / Perulangan (for i in variabel)

# Contoh looping manual
# Ingat! Python adalah bahasa pemrograman yang dijalankan sesuai urutan
print('Looping Manual'.center(40,'='))
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)
print()


# Looping dengan Format Loop
print('Looping dengan format Loop'.center(40,'='))

# Loop list
angka_list = [0,1,2,3,4,5]
print(f'Angka list = {angka_list}')
# Loop
for i in angka_list:
    print(f'Diambil i --> {i}')
print('Selesai.\n')


# Loop Range
angka_range = range(0,6)
print(f'Angka range = {angka_range}')
# loop
for i in angka_range:
    print(f'Diambil i dari range --> {i}')
print('Selesai.\n')


angka_range = range(0,5)
print(f'Angka range = {angka_range}')
# loop
for i in angka_range:
    print(f'Diambil i dari range --> {i}')
print('Selesai.\n')


angka_range = range(0,4)
print(f'Angka range = {angka_range}')
# loop
for i in angka_range:
    print(f'Diambil i dari range --> {i}')
print('Selesai.\n')


angka_range = range(1,10)
print(f'Angka range = {angka_range}')
# loop
for i in angka_range:
    print(f'Diambil i dari range --> {i}')
print('Selesai.\n')


angka_range = range(0,10)
print(f'Angka range = {angka_range}')
# loop
for i in angka_range:
    print(f'Diambil i dari range --> {i}')
print('Selesai.\n')


# Loop String (mengeja)
nama = 'Sakura Haruka'
print(f'Nama: {nama}')
# loop
for huruf in nama:
    print(huruf)
print('Selesai.\n')