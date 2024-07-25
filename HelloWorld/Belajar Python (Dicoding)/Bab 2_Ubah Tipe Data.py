print()

# MENGUBAH TIPE DATA
print("MENGUBAH TIPE DATA".center(40,"-"))

# INTEGER KE STRING
print("INTEGER KE STRING".center(40," "))
angka = 2024
ubah = str(angka)
print(f"Sebelum diubah ke Integer = {angka}")
print(f'Setelah diubah ke Integer = {ubah}')

# STRING KE INTEGER
print("STRING KE INTEGER".center(40," "))
print("Syarat merubah string ke integer: string berupa angka")
teks = "2024"
ubah = int(teks)
print(f"Sebelum diubah ke integer = {teks}")
print(f"Setelah diubah ke integer = {ubah}")

# INTEGER KE FLOAT
print("INTEGER KE FLOAT".center(40," "))
angka = 25
ubah = float(angka)
print(f"Sebelum diubah ke float = {angka}")
print(f"Setelah diubah ke float = {ubah}")

# FLOAT KE INTEGER
print("FLOAT KE INTEGER".center(40," "))
angka = 25.5
ubah = int(angka)
print(f"Sebelum diubah ke integer = {angka}")
print(f"Setelah diubah ke integer = {ubah}")

print()

# MENGUBAH TIPE DATA COLLECTION
print("MENGUBAH TIPE DATA COLLECTION".center(40,"-"))

# LIST KE TUPLE
print("LIST KE TUPLE".center(40," "))
data = [2024, "Haechan", "Umur", 24, True]
ubah = tuple(data)
print(f'Sebelum diubah ke tuple = {data}')
print(f'Setelah diubah ke tuple = {ubah}')

# TUPLE KE LIST
print(f'TUPLE KE LIST'.center(40," "))
data = (1,2,3,4,5,6)
ubah = list(data)
print(f"Sebelum diubah ke list = {data}")
print(f"Setelah diubah ke list = {ubah}")

# LIST KE DICTIONARY
print('LIST KE DICTIONARY'.center(40," "))
print(''' Catatan:
      - Harus ada 2 variabel berbeda
      - variabel yang disebut paling kanan mjd KEY, paling kiri mjd VALUE.
 Contoh 1: ''')
data_1 = ["Jeruk",2]
data_2 = [3,4]
ubah = dict([data_2,data_1])
print(f'Anggota data A = {data_1}')
print(f'Anggota data B = {data_2}')
print(f'Setelah diubah ke Dictionary = {ubah}')
print()

print(" Contoh 2:")
data_2[0] = "Mangga"
ubah = dict([data_2,data_1])
print(f'Anggota data C = {data_1}')
print(f'Anggota data D = {data_2}')
print(f'Setelah diubah ke Dictionary = {ubah}')
