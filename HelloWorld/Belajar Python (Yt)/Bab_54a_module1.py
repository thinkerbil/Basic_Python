# Module program utama

# fungsi tambah
def tambah(*args):
    hasil = 0
    for angka in args:
        hasil += angka
    
    return hasil


# fungsi kali
def kali(*args):
    hasil = 1
    for angka in args:
        hasil *= angka
    
    return hasil


# fungsi pangkat (cara lambda)
def pangkat(n:int):
    return lambda angka:angka**n