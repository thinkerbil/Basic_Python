# Drawing Loop (menggambar segitiga)


# FOR LOOP
print('Menggambar Dengan FOR LOOP'.center(40,'='))

# Contoh 1 -> Segitiga siku-siku
n = 5  # Jumlah baris

for i in range(1, n + 1):
    print('*' * i)



print('\n'*2)
# Contoh 2 --> Segitiga siku-siku terbalik
n = 5  # Jumlah baris

for i in range(n, 0, -1):
    print('*' * i)



print('\n'*2)
# Contoh 3 --> Segitiga sama kaki
n = 5  # Jumlah baris

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))



print('\n'*2)
# Contoh 4 --> Segitiga sama kaki terbalik
n = 5  # Jumlah baris

for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))



print('\n'*2)
# Contoh 5 --> Belah Ketupat (Gabungan Segitiga sama kaki)
n = 5  # Jumlah baris

# Segitiga Bagian atas
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# Segtiga Bagian bawah
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))



print()
# Contoh 6
tinggi_segitiga = int(input('Masukkan tinggi segitiga (dalam satuan baris): '))

for baris in range(1,tinggi_segitiga):
    print('*'*baris)



print()
# Contoh 7
t = int(input('Masukkan tinggi segitiga (dalam satuan baris): '))
for baris in range(1,t + 1):
    print('*'*baris)



print()
# Contoh 8 --> segitiga terbalik
for baris in range(1,t + 1):
    print('*' * (t-baris+1))



print()
# Contoh 9
for baris in range(1,t + 1):
    print((t-baris)* ' ' + (2*baris-1) * '*')



# WHILE LOOP
print('Menggambar Dengan WHILE LOOP'.center(40,'='))

# Contoh 1 --> Segitiga siku-siku
n = 5  # Jumlah baris
i = 1

while i <= n:
    print('*' * i)
    i += 1



print()
# Contoh 2 --> Segitiga siku-siku terbalik
n = 5  # Jumlah baris
i = n

while i > 0:
    print('*' * i)
    i -= 1



print()
# Contoh 3 --> Segitiga sama kaki
n = 5  # Jumlah baris
i = 1

while i <= n:
    print(' ' * (n - i) + '*' * (2 * i - 1))
    i += 1



print()
# Contoh 4 --> Segitiga sama kaki terbalik
n = 5  # Jumlah baris
i = n

while i > 0:
    print(' ' * (n - i) + '*' * (2 * i - 1))
    i -= 1



print()
# Contoh 5 --> Belah ketupat
n = 5  # Jumlah baris
i = 1

# Bagian atas
while i <= n:
    print(' ' * (n - i) + '*' * (2 * i - 1))
    i += 1

i = n - 1

# Bagian bawah
while i > 0:
    print(' ' * (n - i) + '*' * (2 * i - 1))
    i -= 1
