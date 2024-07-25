# TYPE HINTS
# adalah bantuan untuk mengidentifikasi tipe argumen pada fungsi (
# berguna jika semisal sedang sharing program. 
# Alur: Misal tidak pakai type hints. User1 yang membuat program, argumen fungsi nya seharusnya berupa integer,
# Tp ketika sharing program dgn User2, User2 tdk tau kalau ternyata tipe argumennya harusnya integer, shg User2 mengisi argumennya brp string


# Bentuk:
def fungsi(parameter:int):
    hasil = parameter ** 2
    return hasil

print(fungsi(100))
print(fungsi(2))
print(fungsi(True)) # nilai int TRUE adalah 1

# tetapi jika memanggil:
'''
print(fungsi('Ucok'))    # --> akan error, karena 'Ucok' bukan tipe integer (yang diminta adalah argumen bertipe integer)
'''
















