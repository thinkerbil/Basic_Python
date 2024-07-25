print()

# MENGHITUNG PANJANG ELEMENNYA
print("Menghitung panjang / banyaknya elemen".upper().center(60,"-"))
print('''Memakai: len()
  Contoh 1: ''')
list = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6]
hitung = len(list)
print(f'Anggota list = {list}')
print(f'Banyaknya anggota list = {hitung}')
print('Catatan: List akan tetap menghitung data yang double/sama')

print('''
  Contoh 2:''')
set = set([1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6])
hitung = len(set)
print(f'Anggota set = {set}')
print(f'Banyaknya anggota set = {hitung}')
print('Catatan: pada contoh 2, kita memakai anggota list sbg anggota set juga. Lalu, setelah diubah ke set, data yang double mjd tunggal')

print('''
  Contoh 3: ''')
tuple = tuple([1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6])
hitung = len(tuple)
print(f'Anggota tuple = {tuple}')
print(f'Banyaknya anggota tuple = {hitung}')

print('''
  Contoh 4: ''')
string = "Lee Haechan Supremacy"
hitung = len(string)
print(f'Kata = {string}')
print(f'Banyaknya elemen huruf = {hitung}')

print()

# MENGHITUNG NILAI MAX & MIN DARI SUATU DAFTAR ANGKA
print('Menghitung nilai max & min suatu daftar angka'.upper().center(60,"-"))
print('''Memakai: max() & min() 
  Contoh 1: ''')
list = [125, 124, 130, 121, 148, 153, 117, 182, 119, 143]
hitung_maks = max(list)
hitung_min = min(list)
print(f'Anggota list = {list}')
print(f'Nilai maksimum dari list = {hitung_maks}')
print(f'Nilai minimum dari list = {hitung_min}')

print('''
  Contoh 2: ''')
set = {134, 127, 119, 153, 108, 139, 143, 116}
hitung_maks = max(set)
hitung_min = min(set)
print(f'Anggota set = {set}')
print(f'Nilai maksimum dari set = {hitung_maks}')
print(f'Nilai minimum dari set = {hitung_min}')

print('''
  Contoh 3: ''')
tuple = (1123, 1243, 1223, 1321, 1236, 1242, 1142, 1038, 1073, 1609, 1542)
hitung_maks = max(tuple)
hitung_min = min(tuple)
print(f'Anggota tuple = {tuple}')
print(f'Nilai maksimum dari tuple = {hitung_maks}')
print(f'Nilai minimum dari tuple = {hitung_min}')

print()

# MENGHITUNG BANYAKNYA ELEMEN YANG SAMA/DOUBLE BANYAK
print('Menghitung banyaknya elemen yang sama'.upper().center(60,"-"))
print('''Memakai: var.count(data yang mau dicari)
  Contoh 1: ''')
list = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6]
hitung = list.count(6)
print(f'Anggota list = {list}')
print(f'Banyaknya anggota 6 = {hitung}')

print('''
  Contoh 2:''')
kata = 'HAHAHAHAHAHAHHAHAHHAHAHAHAHA'
hitung = kata.count('A')
print(f'Kata = {kata}')
print(f'Banyaknya huruf A = {hitung}')

print()

# MENGECEK ADA/TIDAK ADA NYA SUATU KATA DALAM SUATU VARIABEL
print('Mengecek ada/tidak ada nya suatu kata'.upper().center(60,"-"))
print('''Memakai: 'kata' in variabel 
  Contoh: ''')
kalimat = 'Lee Haechan adalah orang ganteng, kece, badas, woah yang berada di grup NCT.'
cek_1 = 'woah' in kalimat
cek_2 = '.' in kalimat
cek_3 = 'Lee Taeyong' in kalimat
print(f'Kalimat = {kalimat}')
print('Apakah kata berikut ada di kalimat?')
print(f'"Woah" = {cek_1}')
print(f'Tanda (.) = {cek_2}')
print(f'"Lee Taeyong" = {cek_3}')

print('''
Apakah kata berikut tidak ada di kalimat?''')
cek_3 = "Lee Taeyong" not in kalimat
cek_4 = "ganteng" not in kalimat
cek_5 = 'hujan' not in kalimat
cek_6 = 'di' not in kalimat
cek_7 = 'Renjun' not in kalimat
cek_8 = 'jelek' not in kalimat
print(f'"Lee Taeyong" = {cek_3}')
print(f'"ganteng" = {cek_4}')
print(f'"hujan" = {cek_5}')
print(f'"di" = {cek_6}')
print(f'"Renjun" = {cek_7}')
print(f'"jelek" = {cek_8}')



