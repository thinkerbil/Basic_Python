# Penyingkatan dalam Operasi Assignment
print()
print('========== OPERASI ASSIGNMENT =========')
print()

# Assignment biasa
a = 5
print(f'Nilai a = {a}')
a = a + 1
print(f'Assignment biasa: Nilai a = a + 1 adalah {a}')



# Assignment penyingkatan
# ex: a += 1 artinya sama seperti a = a + 1
print()
print('Assignment Penyingkatan:')

# Operasi Biasa
print('======== Operasi Biasa ========')
b = 5
print(f'Nilai b = {b}')

b += 1
print(f'Nilai b += 1 adalah {b}')

b -= 1
print(f'Nilai b -= 1 adalah {b}')

b *= 4
print(f'Nilai b *= 4 adalah {b}')

b /= 2
print(f'Nilai a /= 2 adalah {b}')

b **= 2
print(f'Nilai b **= 2 adalah {b}')

b /= 10
print(f'Nilai b /= 10 adalah {b}')

b //= 3
print(f'Nilai b //= 3 adalah {b}')

b %= 3
print(f'Nilai b %= 3 adalah {b}')



print()
# Operasi Bitwise
print('======== Operasi Bitwise ========')

# Bitwise: OR
print('---- OR ----')
c = True
print(f'Nilai c = {c}')
c |= False
print(f'Nilai c |= False adalah {c}')
print()
d = False
print(f'Nilai d = {d}')
d |= False
print(f'Nilai d |= False adalah {d}')

print()
# Bitwise: AND
print('---- AND ----')
c = True
print(f'Nilai c = {c}')
c &= False
print(f'Nilai c &= False adalah {c}')
print()
d = False
print(f'Nilai d = {d}')
d &= False
print(f'Nilai d &= False adalah {d}')

print()
# Bitwise: XOR
print('---- XOR ----')
c = True
print(f'Nilai c = {c}')
c ^= False
print(f'Nilai c ^= False adalah {c}')
print()
d = True
print(f'Nilai d = {d}')
d ^= True
print(f'Nilai d ^= True adalah {d}')

print()
# Geser-Geser
print('---- Geser Kanan ----')
c = 0b0100
print(f'Nilai c = {c}')
print(f'Nilai c = {format(c,"04b")}')
c >>= 2
print(f'Nilai c >>= 2 adalah {c}')
print(f'Nilai c >>= 2 adalah {format(c,"04b")}')

print()
print('---- Geser Kiri ----')
c = 0b01001
print(f'Nilai c = {c}')
print(f'Nilai c = {format(c,"05b")}')
c <<= 1
print(f'Nilai c <<= 1 adalah {c}')
print(f'Nilai c <<= 1 adalah {format(c,"05b")}')