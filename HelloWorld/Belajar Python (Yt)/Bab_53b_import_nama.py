# nama_1 = 'Sakura'
# nama_2 ='Ucup'


n = int(input('masukkan angka: '))

def temukandigitnol(n):
    x = 0
    y = 5

    if n < 0:
        return "error"
    
    while (n//y)>0:
        x += n//y
        y *= 5
        return x
    
print(temukandigitnol(n))