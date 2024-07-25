# BREAK

# skip aksi selanjutnya jika permintaan khusus sudah terpenuhi (langsung finish proses/program)

# Lihat perbedaan antara continue dengan break
# Contoh 1 --> memakai continue
print('Contoh 1 Break (Continue)'.center(40,'='))
angka = 0

while angka < 5:
    angka += 1
    print(f'Angka sekarang = {angka}')

    if angka == 3:
        print('Nice!')
        continue

    print('Shaaappp!!')

print('Beres.\n')


# Contoh 2 --> break ketika angka = 3 (angka 4 dan 5 di skip) --> langsung finish
print('Contoh 2 Break'.center(40,'='))
angka = 0

while angka < 5:
    angka += 1
    print(f'Angka sekarang = {angka}')

    if angka == 3:
        print('Nice!')
        break

    print('Shaaappp!!')

print('Beres.\n')


# Contoh 3 --> Break nya di-comment
print('Contoh 3 Break (break di-comment)'.center(40,'='))
angka = 0

while angka < 5:
    angka += 1
    print(f'Angka sekarang = {angka}')

    if angka == 3:
        print('Nice!')
        # break

    print('Shaaappp!!')

print('Beres.\n')


# Contoh 4 --> walau angka input nya >10, tetap akan dieksekusinya hanya sampai 10
print('Contoh 4 Break'.center(40,'='))

angka = 0
data = int(input('Hitung sampai angka = '))

while angka < 10:
    angka += 1
    print(f'Angka sekarang = {angka}')

    if angka == data:
        print('Nice!')
        break

    print('Shaaappp!!')

print('Beres.\n')


# Contoh 5 --> akan dihitung sampai angka yang input (karena syarat while nya adanya ketika 'True' dimana True >= 1)
print('Contoh 5 Break'.center(40,'='))

angka = 0
data = int(input('Hitung sampai angka = '))

while True:
    angka += 1
    print(f'Angka sekarang = {angka}')

    if angka == data:
        print('Nice!')
        break

    print('Shaaappp!!')

print('Beres.\n')
