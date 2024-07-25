# Membuat Kalkulator Sederhana

# Penerapan If, Else, Elif

print('Kalkulator Sederhana'.center(40,'='))
angka_1 = float(input('Masukkan angka: '))
operator = input('Masukkan operasinya (+,-,x,/): ')
angka_2 = float(input('Masukkan angka lagi: '))

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'Hasil: {angka_1} + {angka_2} = {hasil}' )
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'Hasil: {angka_1} - {angka_2} = {hasil}')
elif operator == 'x' or '*':
    hasil = angka_1 * angka_2
    print(f'Hasil: {angka_1} x {angka_2} = {hasil}')
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f'Hasil: {angka_1} / {angka_2} = {hasil}')
else:
    print('Tulis yang bener, bang!')

print('Terima kasihtelah memilih layanan kami^^')