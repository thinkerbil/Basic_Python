print('=================== OPERASI ARITMETIKA ==================')
# Penjumlahan (+)
# Pengurangan (-)
# Perkalian (*)
# Pembagian (/)
# Eksponen or Pangkat (**)
# Modulus or Modulo or Sisa Pembagian (%)
# Floor Division or Pembulatan ke bawah (//)

# Prioritas hitung:
'''
1. ( )
2. Eksponen **
3. Perkalian pembagian, dkk. * / % //
4. Pertambahan Pengurangan + -
'''

a = 20
b = 2
c = 4

hasil = a + b
print(f'{a} + {b} = {hasil}')

hasil = a - b
print(f'{a} - {b} = {hasil}')

hasil = a * b
print(f'{a} * {b} = {hasil}')

hasil = a / b
print(f'{a} / {b} = {hasil}')

hasil = a ** b
print(f'{a} ** {b} = {hasil}')

hasil = a % b
print(f'{a} & {b} = {hasil}')

hasil = a // b
print(f'{a} // {b} = {hasil}')

hasil = a + b * c
print(f'{a} + {b} * {c} = {hasil}')

hasil = (a - b) * b + (c - b)
print(f'{(a - b)} * {b} + {(c - b)} = {hasil}')

hasil = (a + b) / b + a // b % b * a
print(f'{(a + b)} / {b} + {a} // {b} % {b} * {a} = {hasil}')


