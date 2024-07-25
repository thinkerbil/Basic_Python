# CONTINUE & PASS

# While Loop Biasa
angka = 0
print(f'Angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print(f'Angka sekarang --> {angka}')
    print('Arigatou')
print('Beres.\n')



# PASS --> tidak dieksekusi
# untuk mengisi isian dari 'fungsi' apabila 'fungsi' tsb ga ada isi nya
angka = 0
print(f'Angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print(f'Angka sekarang -> {angka}')

    if angka == 3:
        pass

    print('Nice! Arigatou!')
print('Beres.\n')



# CONTINUE --> Loop di dalam Loop

# Perhatikan perbedan contoh 1 dan contoh 2 di bawah

# Contoh 1 --> Tidak ada Continue
print('Contoh 1 CONTINUE'.center(40,'='))

angka = 0
print(f'Angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print(f'Angka sekarang -> {angka}')

    if angka == 3:
        print('OKEE!!')

    print('Nice! Arigatou!')
print('Beres.\n')


# Contoh 2 --> ada Continue di if (di bawah print) --> "Nice! Arigatou!" nya dilewat, langsung lanjut ke angka 4
print('Contoh 2 CONTINUE'.center(40,'='))
angka = 0
print(f'Angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print(f'Angka sekarang -> {angka}')

    if angka == 3:
        print('OKEE!!')
        continue

    print('Nice! Arigatou!')
print('Beres.\n')


# COntoh 3 --> Continue di atas print "OKEEE!" --> "OKEEE!" nya dilewat. langsung lanjut ke angka 4
print('Contoh 3 CONTINUE'.center(40,'='))
angka = 0
print(f'Angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print(f'Angka sekarang -> {angka}')

    if angka == 3:
        continue
        print('OKEE!!')

    print('Nice! Arigatou!')
print('Beres.\n')


# COntoh 4 --> Print "angka sekarang" milik While di bawah Continue --> print angka 3 di skip
print('Contoh 4 CONTINUE'.center(40,'='))
angka = 0
print(f'Angka sekarang -> {angka}')

while angka < 5:
    angka += 1

    if angka == 3:
        continue
        print('OKEE!!')

    print(f'Angka sekarang -> {angka}')
    print('Nice! Arigatou!')
print('Beres.\n')
