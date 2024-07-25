# DICTIONARY / DICT
print('DICTIONARY'.center(20,'='))

# Dictionary = data collection yang bukan pake index, tapi pake 'key' apabila ingin memanggil
# Identifier --> key

# Bentuk
data_dict = {
    'key': 'value',
    'skr': 'sakura',
    'ummy': 'umemiya',
    'nbl': 'nabila',
    'nmr': 127,
    'list': [1,2,4,6,8,10]
}

print(f'''Mengakses Value / Panggil Key data dictionary:
key "skr" --> {data_dict['skr']}
key "nmr" --> {data_dict["nmr"]}
key "list" --> {data_dict["list"]}''')
