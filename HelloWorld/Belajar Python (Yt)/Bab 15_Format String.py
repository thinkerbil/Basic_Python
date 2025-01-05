# Format-Format Pada String

# Cara mudah menulis assignment

# Contoh 1
nama = 'Haruka'
umur = 17
contoh_format = f'Biodata: {nama}, {umur}'
print(contoh_format)

# Contoh 2
print(f'Biodat: Haruka, {umur}')
print(f'Biodata: {nama}, {umur}')

# Contoh 3: Boolean
boolean = True
print(f'Nilai Boolean: {boolean}')

# Format Angka

# Format untuk angka bilangan bulat (:d) --> jika angkanya bil desimal, akan error
angka = 15
print(f'Angka bilangan bulat = {angka:d}')



# Format untuk ordo ribuan (:,) --> otomatis ngasih koma
ribuan_1 = 2000
ribuan_2 = 50000
jutaan_1 = 2000000
jutaan_2 = 50000000
print(f'Ribuan = {ribuan_1:,}')
print(f'Ribuan = {ribuan_2:,}')
print(f'Jutaan = {jutaan_1:,}')
print(f'Jutaan = {jutaan_2:,}')

print()



# Format untuk angka desimal (:.nf) --> n = berapa angka di belakang koma
desimal = 1234.56789
print(f'Angka desimal = {desimal:.2f} --> (:.2f) dua angka di belakang koma')
print(f'Angka desimal = {desimal:.3f} --> (:.3f) tiga angka di belakang koma')

print()



# Format angka desimal: Menampilkan leading Zero (:m.nf) / (:0m.nf) --> m = jumlah karakter yang mau dimunculin, 0 = karakter pengganti spasi
desimal_1 = 1234.56789
desimal_2 = 5678.5234
print(f'Contoh desimal 1 = {desimal_1}')
print(f'7 karakter, 2 angka setelah koma = {desimal_1:7.2f} --> dibulatkan ke atas 2 angka setelah koma')
print(f'7 karakter, 3 angka setelah koma = {desimal_1:7.3f} --> dibulatkan ke atas 3 angka setelah koma')
print(f'5 karakter, 1 angka setelah koma = {desimal_1:5.1f} --> dibulatkan ke atas 1 angka setelah koma')
print(f'4 karakter, 0 angka setelah koma = {desimal_1:4.0f} --> dibulatkan ke atas')
print(f'5 karakter, 0 angka setelah koma = {desimal_1:5.0f} --> 1 spasi di depan sbg karakter penambah agar memenuhi syarat 5 karakter')
print(f'7 karakter, 0 angka setelah koma = {desimal_1:7.0f} --> 2 spasi di depan sbg karakter penambah agar memenuhi syarat 7 karakter')
print(f'7 karakter, 0 angka setelah koma = {desimal_1:07.0f} --> 0 di depan sbg karakter penambah agar memenuhi syarat 7 karakter')
print()
print(f'Conroh desimal 2 = {desimal_2}')
print(f'7 karakter, 2 angka setelah koma = {desimal_2:7.2f} --> ga dibulatkan')
print(f'7 karakter, 3 angka setelah koma = {desimal_2:7.3f} --> ga dibulatkan')
print(f'5 karakter, 1 angka setelah koma = {desimal_2:5.1f} --> ga dibulatkan')
print(f'4 karakter, 0 angka setelah koma = {desimal_2:4.0f} --> dibulatkan ke atas')
print(f'5 karakter, 0 angka setelah koma = {desimal_2:5.0f} --> 1 spasi di depan sbg karakter penambah agar memenuhi syarat 5 karakter')
print(f'7 karakter, 0 angka setelah koma = {desimal_2:7.0f} --> 2 spasi di depan sbg karakter penambah agar memenuhi syarat 7 karakter')
print(f'7 karakter, 0 angka setelah koma = {desimal_2:07.0f} --> 0 di depan sbg karakter penambah agar memenuhi syarat 7 karakter')

print()



# Menampilkan tanda plus / minus angka (:+d)
angka_minus = -10
angka_plus_1 = 10
angka_plus_2 = 10.1234
print(f'Angka minus = {angka_minus}')
print(f'Angka minus pake format = {angka_minus:+d}')
print(f'Angka plus = {angka_plus_1}')
print(f'Angka plus pake format = {angka_plus_1:+d}')
print(f'Angka plus = {angka_plus_2}')
print(f'Angka plus pake format = {angka_plus_2:+.2f}')
print(f'Angka plus pake format = {angka_plus_2:+6.3f}')

print()



# Format merubah ke bentuk persen (:%) / (:.n%) --> n = menampilkan berapa angka yang muncul setelah koma
angka = 0.045
print(f'Angka = {angka}')
print(f'Persen angka = {angka:%}')
print(f'Persen angka = {angka:.1%}')
print(f'Persen angka = {angka:.0%}')
print()
angka = 451.1234
print(f'Angka = {angka}')
print(f'Persen angka = {angka:%}')
print(f'Persen angka = {angka:.1%} --> 1 angka setelah koma')
print(f'Persen angka = {angka:.2%} --> 2 angka setelah koma')
print(f'Persen angka = {angka:.0%} --> 0 angka setelah koma')
print(f'Persen angka = {angka:6.2%}')
print(f'Persen angka = {angka:6.1%}')
print(f'Persen angka = {angka:6.0%}')

print()

# Melakukan operasi aritmatika pada format
harga_barang = 17300
jumlah_barang = 5
print(f'Harga barang = {harga_barang}')
print(f'Jumlah barang = {jumlah_barang}')
print(f'Total harga yang harus dibayar = Rp {harga_barang*jumlah_barang}')
print(f'Total harga yang harus dibayar = Rp {harga_barang*jumlah_barang:,} --> dikasih koma')

print()

# Format angka lain: Binary / Octal / hexadecimal --> bin(variabel) / oct(variabel) / (hex(variabel))
angka = 123
print(f'Angka = {angka}')
print(f'Format Binary = {bin(angka)}')
print(f'Format Octal = {oct(angka)}')
print(f'Format Hexadecimal = {hex(angka)}')




