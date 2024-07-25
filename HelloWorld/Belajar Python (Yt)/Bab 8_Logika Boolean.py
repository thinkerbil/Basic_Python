# Operasi Logika feat. Boolean / Logika Kebenaran
# "NOT", "OR", "AND", "XOR"


# NOT
print('======== NOT ========')
p = True
r = not p
print(f'data p = {p}')
print(f'data r = {r}')

# OR (salah satu TRUE => nilainya TRUE)
print()
print('======== OR ========')
p = True
q = True
r = p or q
print(f'{p} or {q} = {r}')

p = True
q = False
r = p or q
print(f'{p} or {q} = {r}')

p = False
q = True
r = p or q
print(f'{p} or {q} = {r}')

p = False
q = False
r = p or q
print(f'{p} or {q} = {r}')


# AND (Salah satu FALSE => nilainya FALSE)
print()
print('======== AND ========')
p = True
q = True
r = p and q
print(f'{p} and {q} = {r}')

p = True
q = False
r = p and q
print(f'{p} and {q} = {r}')

p = False
q = True
r = p and q
print(f'{p} and {q} = {r}')

p = False
q = False
r = p and q
print(f'{p} and {q} = {r}')


# XOR (yang kembar => nilainya FALSE)
print()
print('======== XOR ========')
p = True
q = True
r = p ^ q
print(f'{p} xor {q} = {r}')

p = True
q = False
r = p ^ q
print(f'{p} xor {q} = {r}')

p = False
q = True
r = p ^ q
print(f'{p} xor {q} = {r}')

p = False
q = False
r = p ^ q
print(f'{p} xor {q} = {r}')