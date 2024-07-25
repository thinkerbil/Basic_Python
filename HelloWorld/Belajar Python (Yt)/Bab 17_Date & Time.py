# DATE AND TIME

# format penulisan memunculkan tanggal

# 1.
import datetime
tanggal_hari_ini = datetime.date.today()
print(f'Tanggal hari ini: {tanggal_hari_ini} \t\t--> tidak dimisalkan')

# 2.
import datetime as dt
tanggal_hari_ini = dt.date.today()
print(f'tanggal hari ini: {tanggal_hari_ini:%A}, {tanggal_hari_ini} --> dimisalkan "dt"')

# 3. Bila data dari input user
import datetime as dt
tanggal_lahir = int(input('Masukkan tanggal lahir Anda\t: '))
bulan_lahir = int(input('Masukkan bulan lahir Anda\t: '))
tahun_lahir = int(input('Masukkan tahun lahir Anda\t: '))
tanggal_kelahiran = (dt.date(tahun_lahir, bulan_lahir, tanggal_lahir))
print(f'Tanggal lahir Anda adalah\t: {tanggal_kelahiran}')

# 4. Format mengetahui hari suatu tanggal (:%A)
print(f'Anda lahir pada hari\t\t: {tanggal_kelahiran:%A}')

# 5. apabila digabung antara hari dengan tanggal
print(f'Anda lahir pada\t\t\t: {tanggal_kelahiran:%A}, {tanggal_kelahiran}')


# Menghitung Umur
tanggal_hari_ini = dt.date.today()
tanggal_kelahiran = (dt.date(tahun_lahir, bulan_lahir, tanggal_lahir))
umur_dalam_hari = tanggal_hari_ini - tanggal_kelahiran
print(f'Anda berumur\t\t\t: {umur_dalam_hari} \t--> dalam hari')

# Umur dalam satuan tahun (.days)
umur_dalam_hari = tanggal_hari_ini - tanggal_kelahiran
umur_dalam_tahun_1 = umur_dalam_hari / 365
print(f'Anda berumur\t\t\t: {umur_dalam_tahun_1}  --> masih ada "days" nya/ masih dalam hari')

umur_dalam_hari = tanggal_hari_ini - tanggal_kelahiran
umur_dalam_tahun_2 = umur_dalam_hari.days / 365
print(f'Anda berumur\t\t\t: {umur_dalam_tahun_2} tahun  --> ada koma-komaan')

umur_dalam_hari = tanggal_hari_ini - tanggal_kelahiran
umur_dalam_tahun_3 = umur_dalam_hari.days // 365
print(f'Anda berumur\t\t\t: {umur_dalam_tahun_3} tahun \t--> dengan pembagian ke bawah (//)')