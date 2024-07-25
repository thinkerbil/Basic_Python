# Setiap hasil dari operasi komparasi adalah Boolean (True / False)
# Komparasi meliputi: > , < , >= , <= , == , != , is , is not

a = 5
b = 6
print(f'a = {a}')
print(f'b = {b}')
print()


# Lebih dari (>)
print('==== Lebih dari (>) ====')
x = a > 3
print(f'x = {a} > 3')
print( a > 3)

print()
y = b > 7
print(f'y = {b} > 7')
print(b > 7)

print()
z = a > 5
print(f'z = {a} > 5')
print(a > 5)



# Kurang dari (<)
print()
print('==== Kurang Dari (<) ====')
x = b < 4
print(f'x = {b} < 4')
print(b < 4)

print()
y = a < 8
print(f'y = {a} < 8')
print(a < 8)

print()
z = b < 6
print(f'z = {b} < 6')
print(b < 6)



# Lebih dari Sama dengan (>=)
print()
print('==== Lebih dari sama dengan (>=) ====')
x = a >= 4
print(f'x = {a} >= 4')
print(a >= 4)

print()
y = b >= 9
print(f'y = {b} >= 9')
print(b >= 9)

print()
z = b >= 6
print(f'z = {b} >= 6')
print(b >= 6)



# Kurang dari sama dengan (<=)
print()
print('==== Kurang dari sama dengan (<=) ====')
x = a <= 5
print(f'x = {a} <= 5')
print(a <= 5)

print()
y = a <= 6
print(f'y = {a} <= 6')
print(a <= 6)

print()
z = b <= 4
print(f'z = {b} <= 4')
print(b <= 4)



# Sama Dengan (==)
print()
print('==== Sama dengan (==) ====')
x = a == 5
print(f'x = {a} == 5')
print(a == 5)

print()
y = b == 6
print(f'y = {b} == 6')
print(b == 6)

print()
z = a == 4
print(f'z = {a} == 4')
print(a == 4)



# Tidak sama dengan (!=)
print()
print('==== Tidak Sama Dengan (!=) ====')
x = a != 5
print(f'x = {a} != 5')
print(a != 5)

print()
y = b != 7
print(f'y = {b} != 7')
print(b != 7)



# "is" sbg Komparasi Object Identity
# hex untuk memeriksa identitas
print()
print('==== Komparasi Object Identity "is" ====')
x = 5
y = 5
print(f'x = {x}')
print(f'y = {y}')

print()
print(f'User ID-x = {hex(id(x))}')
print(f'User ID-y = {hex(id(y))}')

print()
print(f'{x} is {y}')
print(x is y)
print(hex(id(x)) == hex(id(y)))

print()
print('==================')
x = 5
y = 7
print(f'x = {x}')
print(f'y = {y}')

print()
print(f'User ID-x = {hex(id(x))}')
print(f'User ID-y = {hex(id(y))}')

print()
print(f'{x} is {y}')
print(x is y)
print(hex(id(x)) == hex(id(y)))


# "is not"
# sama kayak "is" cara kerjanya
print()
print('==== Komparasi "is not" ====')
x = 5
y = 6
print(f'x = {x}')
print(f'y = {y}')

print()
print(f'User ID-x = {hex(id(x))}')
print(f'User ID-y = {hex(id(y))}')

print()
print(f'{x} is not {y}')
print(x is not y)
print(hex(id(x)) != hex(id(y)))