# IF & ELSE Statements (percabangan)

# IF STATEMENTS
# Sesuai nama
nama = input('Masukkan nama Anda: ')
print(f'Nama Anda adalah: {nama}')

if nama == "Sakura": print('Jangan gelut terus, bro!!')
print(f'Halo {nama}!!')

print()
# Tidak sesuai nama
nama = input('Masukkan nama Anda: ')
print(f'Nama Anda adalah: {nama}')

if nama == "Sakura": print('Jangan gelut terus, bro!!')
print(f'Halo {nama}!!')

print()

# IF indentation
nama = input('Masukkan nama Anda: ')
if nama == "Sakura":
    print('YOU\'RE COOL!!')
    print('KEREN ABIEZZZZ!!')
print(f'Oke, Terima kasih {nama}. Semoga harimu menyenangkan!')


# ELSE STATEMENTS
nama = input('Masukkan nama Anda: ')
if nama == "Sakura":
    print('YOU\'RE COOL!!')
    print('KEREN ABIEZZZZ!!')
else:
    print('Oh.')
    print('Oke.')
print('Terima kasih. \n')


# ELIF (Percabangan tapi banyak)

# Elif bisa ditambah sebanyak mungkin

nama = input('Siapa namanya? ')

if nama=='Sakura':
    print('Kakkkoeee!!')
    print('BOFURIN!! GO!!')
elif nama == 'Umemiya':
    print('Menyala ketua!!')
elif nama == 'Gojo':
    print('Bang, bangun bang.')
else:
    input('Hitung: Γ(5) = ')
    print('Hore!! Anda benar! 100!!')

print('Sip.')
