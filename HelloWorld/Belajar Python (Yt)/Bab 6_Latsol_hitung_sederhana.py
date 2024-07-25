# Latsol Mengonversi Temperatur ke temperatuur lain

print()
print('====================== PROGRAM KONVERSI TEMPERATUR ========================')
print()

# Celcius ke temperatur lain
celcius = float(input('Diketahui suhu dalam celcius adalah: '))
print(f'Suhu dalam celcius = {celcius} Celcius')

# Celcius -> Reamur
reamur = (4/5) * celcius
print(f'Suhu dalam Reamur = {reamur} Reamur')

# Celcius -> Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print(f'Suhu dalam Fahrenheit = {fahrenheit} Fahrenheit')

# Celcius -> Kelvin
kelvin = celcius + 273
print(f'Suhu dalam Kelvin = {kelvin} Kelvin')



print()
print('==== Reamur ke Temperatur Lain ====')
print()

reamur = float(input("Diketahui suhu dalam reamur adalah: "))
print(f'Suhu dalam Reamur = {reamur} Reamur')

# Reamur -> Celcius
celcius = (5/4) * reamur
print(f'Suhu dalam Celcius = {celcius} Celcius')

# Reamur -> Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print(f'SUhu dalam Fahrenheit = {fahrenheit} Fahrenheit')

# Reamur -> Kelvin
kelvin = ((5/4) * reamur) + 273
print(f'Suhu dalam Kelvin = {kelvin} Kelvin')



print()
print('==== Fahrenheit ke Temperatur Lain ====')
print()

fahrenheit = float(input('Diketahui suhu dalam Fahrenheit adalah: '))
print(f'Suhu dalam Fahrenheit = {fahrenheit} Fahrenheit')

# Fahrenheit -> Celcius
celcius = 5/9 * (fahrenheit - 32)
print(f'Suhu dalam Celcius = {celcius} Celcius')

# Fahrenheit -> Reamur
reamur = (4/9) * (fahrenheit - 32)
print(f'Suhu dalam Reamur = {reamur} Reamur')

# Fahrenheit -> Kelvin
'''
1. fahrenheit -> Celcius
2. celcius -> kelvin
'''

kelvin = (5/9 * (fahrenheit - 32)) + 273
print(f'Suhu dalam kelvin = {kelvin} Kelvin')




print()
print('==== Kelvin ke Temperatur Lain ====')
print()

kelvin = float(input('Diketahui suhu dalam Kelvin adalah: '))
print(f'Suhu dalam Kelvin = {kelvin} Kelvin')

# kelvin -> Celcius
celcius = kelvin - 273
print(f'Suhu dalam Celcius = {celcius} Celcius')

# Kelvin -> Reamur
reamur = 4/5 * (kelvin - 273)
print(f'Suhu dalam Reamur = {reamur} Reamur')

# Kelvin -> Fahrenheit
'''
1. Kelvin -> Celcius -> (K - 273)
2. Celcius -> Fahrenheit
'''
fahrenheit = ((9/5) * (kelvin - 273)) + 32
print(f'Suhu dalam Fahrenheit = {fahrenheit} Fahrenheit')