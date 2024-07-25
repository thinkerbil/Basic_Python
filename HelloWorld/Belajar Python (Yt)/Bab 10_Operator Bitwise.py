# 1 = 2^0 = 00000001
# 2 = 2^1 = 00000010
# 4 = 2^2 = 00000100
# 3 = 2+1 = 2^1 + 2^0 = 00000010 + 00000001

print()
print("========== OPERATOR BITWISE ==========")
print()

a = 9
b = 5

# Bitwise OR (|)
print('========= OR ========')
# ex: a | b  ----> dihitung dengan cara: operasi OR 
c = a|b
print(f'Nilai: {a}, binary: {format(a,"08b")}')
print(f'Nilai: {b}, binary: {format(b,"08b")}')
print('-------------------------------(|)')
print(f'Nilai: {c}, binary: {format(c,"08b")}')


print()
# Bitwise AND (&)
print('========= AND ========')
# ex: a & b -----> dihitung dengan cara: operasi AND
c = a & b
print(f'Nilai: {a}, binary: {format(a,"08b")}')
print(f'Nilai: {b}, binary: {format(b,"08b")}')
print('-------------------------------(&)')
print(f'Nilai: {c}, binary: {format(c,"08b")}')


print()
# Bitwise XOR(^)
print('========= XOR ========')
# ex: a & b -----> dihitung dengan cara: operasi XOR
c = a ^ b
print(f'Nilai: {a}, binary: {format(a,"08b")}')
print(f'Nilai: {b}, binary: {format(b,"08b")}')
print('-------------------------------(^)')
print(f'Nilai: {c}, binary: {format(c,"08b")}')


print()
# Bitwise NOT(~)
print('========= NOT ========')
# ex: ~a -----> dihitung dengan cara: operasi NOT
c = ~a
print(f'Nilai: {a}, binary: {format(a,"08b")}')
print('-------------------------------(~)')
print(f'Nilai: {c}, binary: {format(c,"08b")}')


print()
# Bitwise SHIFT RIGHT(>>)
print('===== SHIFT RIGHT =====')
# ex: a >> 2 ----> nilai bitwise "a" geser 2 ke kanan
c = a >> 2
print(f'Nilai: {a}, binary: {format(a,"08b")}')
print('-------------------------------(>>)')
print(f'Nilai: {c}, binary: {format(c,"08b")}')

d = a >> 3
print(f'Nilai: {d}, binary: {format(d,"08b")}')

print()
# Bitwise SHIFT LEFT(<<)
c = a << 2
print(f'Nilai: {a}, binary: {format(a,"08b")}')
print('-------------------------------(<<)')
print(f'Nilai: {c}, binary: {format(c,"08b")}')