nama = 'Umemiya'
print(f'{nama}, tipe: {type(nama)}')

print()
print('=========== Serba-Serbi String ===========')
print()

# 1. Basic
'''
1. pake single quote: '...'
2. pake double quote: "..."
3. pake dua-duanya: "...'..." atau '..."..."...'
'''
print('ini pake single quote')
print("ini pake double quote")
print('"Halo, Umemiya!" --> ini make combo quote')
print("Hari ini hari Jum'at --> ini diselipin 1 single quote")


# 2. Menggunakan Tanda (\) di Kasus Khusus

# Membuat tanda (') menjadi string
print('Hari ini hari Jum\'at')
print('g\'day, isn\'t it?')

# Membuat Tanda Backslash (\) Menjadi String
# caranya: di-double backslash (\\)
print('contoh letak file --> C:\\User\\Umemiya')

# Membuat Tab (\t) antar kata se-line
print('Sakura\t\tHaruka --> ini pake Tab') 

# Membuat Backspace (\b) antar kata se-line
print('Sakura \bHaruka --> ini pake backspace')

# Membuat newline (\n) atau (\r\n)
print('baris pertama.\nbaris kedua.  --> ini LF (\\n): untuk Mac, Linux')
print('baris pertama.\rbaris kedua.  --> ini CR (\\r): untuk model lama')
print('baris pertama.\r\nbaris kedua.  --> ini CRLF (\\r\\n): untuk windows')

# 3. String Literal atau Raw

# Multiline Literal String
print('''
Nama: Sakura Haruka
Kelas: 1 SMA
--> ini pake Multiline Literal String biasa
''')

# Menggunakan Raw String ("r" di depan string)
# Otomatis semuanya dianggap string
print(r'Ini string literal --> pake "r" di depan string.')
print(r'hari jumat.\nHari yang indah.  --> pake "r" di depan.')
print(r'''
Nama: Sakura Haruka
Kelas: 1 SMA
Website: www.sakuraharuka.com\newID
--> ini pake multiline literal raw string ("r" di depan)
''')

