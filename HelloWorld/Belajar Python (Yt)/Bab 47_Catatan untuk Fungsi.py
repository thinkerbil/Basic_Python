# PERHATIKAN!

'''
def fungsi(parameter):
    hasil = parameter**2
    return hasil

fungsi(2)
'''
# bentuk seperti di atas tidak akan keluar output nya


# kecuali:
'''
def fungsi(parameter):
    hasil = parameter**2
    return hasil

y = fungsi(2)
print(y)
'''
# pemanggilan fungsinya dibuatkan variabel, agar si 'return' nya berjalan, baru deh ketik 'print'


# atau:
'''
def fungsi(parameter):
    hasil = parameter**2
    print hasil

fungsi(2)
'''
# pada isi fungsi, bukan ketik 'return' tapi langsung 'print'. lalu pada pemanggilan, hanya manggil fungsi saja, tanpa dibuatkan variabel


# kalau tidak percaya, silahkan dibuka masing2 kutip nya