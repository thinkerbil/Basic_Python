#ini comment

# TIPE DATA
print("TIPE DATA".center(40,"-"))

# STRING
teks = "Halo!"
print(f"Ini tipe data string = {teks}")

# INTEGER
angka = 2024
print(f"Ini tipe data Integer = {angka}")

# FLOAT
angka = 12345678.9
print(f"Ini tipe data Float = {angka}")

# BOOLEAN
pilih_1 = True
pilih_2 = False
print(f"Ini tipe data Boolean = {pilih_1}")
print(f"Ini tipe data Boolean = {pilih_2}")

print()


#INDEKS STRING
print("INDEKS PADA STRING".center(40,"-"))
print("Indeks pada string dimulai dari indeks ke-0")
bulan = "Februari"
print(f"Contoh kata = {bulan}")
print(f"Indeks ke-0 = {bulan[0]}")
print(f"Indeks ke-3 = {bulan[3]}")
print(f"Indeks dari 3 ke kanan = {bulan[3:]}")
print(f"3 huruf di depan = {bulan[:3]}")

print()


# TIPE DATA COLLECTION
print("TIPE DATA COLLECTION".center(40,"-"))

#LIST
print("Tipe Data LIST".ljust(40,"-"))
data_list = [1, "Juned", "Mangga", 2]
print(f"Sebelum diubah = {data_list}")
print(''' Catatan:
      - memakai kurung siku
      - memiliki indeks, dimulai dari indeks ke-0
      - tiap elemen pada data list bisa diubah.
Contoh: ''')
data_list[3] = 4
print(f'Setelah diubah = {data_list}') 

print()

#TUPLE
print("Tipe Data TUPLE".ljust(40,"-"))
data_tuple = (2, "Haechan", 2, "Renjun")
print(f"Data tuple : {data_tuple} --> Memakai kurung bulat")
print(''' Catatan:
      tiap elemen pada data tuple tidak bisa diubah. ''')

print()

#SET
print("Tipe Data SET".ljust(40,"-"))
data_set = {1, 2, 1, 2, 3, 4, 3, 5, 6, 6}
print(f"Data Set : {data_set} --> Memakai kurung kurawal seperti himpunan.")

print()

#DICTIONARY
print("Tipe Data Dictionary".ljust(40,"-"))
print("Aturan penulisan tipe data Dictionary:")
print('''- Memakai kurung kurawal
- Memiliki key-value
- Antara key & value dipisah dgn titik dua (:)
- Key-value satu dgn yang lainnya dipisah dgn koma (,)
- Key & value jenis tipe datanya apa aja.
Contoh: ''')
data_dictionary = {"Nama" : "Haechan", "Umur" : 24, "Menikah" : False}
print(f"Data Dictionary : {data_dictionary}")

print()
print('Catatan:')
print('''  Pada data dictionary, VALUE BISA DIUBAH dgn cara: 
ketik: variabel['Key'] = 'value baru'
Contoh: ''')
data_dictionary["Nama"] = "Jaehyun"
print(f"Perubahan Nama = {data_dictionary}")

print()