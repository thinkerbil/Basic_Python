print('==================== INPUT DATA ====================')

# INPUT DATA tipenya selalu DATA STRING
nama = input('Nama kamu siapa? ')
alamat = input("Kamu tinggal di mana?")
kegiatan = input('Apa kegiatanmu akhir-akhir ini?')
# cara kerja: klik enter pada space running agar sistemnya jalan (muncul pertanyaan selanjutnya).
# habis meng-input data pada space run, habis itu datanya dipanggil dengan cara ketik Print.
# dan untuk memunculkan bagian "print", klik enter juga yeah.
print('==============================')
print('Apakah benar data Anda seperti berikut?')
print(f'Nama = {nama}')
print(f'Alamat = {alamat}')
print(f'Kegiatan = {kegiatan}')

# input data selalu bertipe DATA STRING (karakter)
# jika ingin menginput angka, harus dikonversi dulu / diturunkan dulu (sistem fog)

print()
angka = input('Masukkan angka = ')
print(f'Data = {angka}, tipe data: {type(angka)}')

print()
angka = int(input('Masukkan angka = '))
print(f'Data = {angka}, tipe data: {type(angka)}')

print()
angka = float(input('Masukkan angka = '))
print(f'Data = {angka}, tipe data: {type(angka)}')

print()
angka = float(int(input('Masukkan angka = ')))
print(f'Data = {angka}, tipe data: {type(angka)}')

print()
angka = bool(int(input('Masukkan angka = ')))
print(f'Data = {angka}, tipe data: {type(angka)}')

print()