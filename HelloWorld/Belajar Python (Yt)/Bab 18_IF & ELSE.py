# IF & ELSE Statements (percabangan)

# IF STATEMENTS
# Sesuai Nama
nama = input('Masukkan nama Anda: ')
print(f'Nama Anda adalah: {nama}')

if nama == "Sakura": print('Jangan gelut terus, bro!!')
print(f'Halo {nama}!!\n')

# Tidak Sesuai Nama
nama = input('Masukkan nama Anda: ') # --> Masukkan nama selain "Sakura"
print(f'Nama Anda adalah: {nama}')

if nama == "Sakura": print('Jangan gelut terus, bro!!') # --> outputnya tidak akan mem-print 'Jangan gelut terus, bro!!'
print(f'Halo {nama}!!\n') # Output hanya akan mem-print baris ini saja


# IF INDENTATION
nama = input('Masukkan nama Anda: ')
if nama == "Sakura":
    print('YOU\'RE COOL!!')
    print('KEREN ABIEZZZZ!!')
print(f'Oke, Terima kasih {nama}. Semoga hari mu menyenangkan!')


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
