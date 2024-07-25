# MODULE (import module) DAN ALIAS (as)
# digunakan jika file nya sejajar / keduanya (file module & file utama program) sama2 berbentuk file yg ada di dalam satu folder yg sama

import os
os.system('cls')

# dgn cara import
import Bab_54a_module1

hasil_pertambahan = Bab_54a_module1.tambah(1,2,3,4,5,6,7,8)
print(f'Hasil pertambahan = {hasil_pertambahan}')

hasil_perkalian = Bab_54a_module1.kali(1,2,3,4,5,6,7)
print(f'Hasil perkalian = {hasil_perkalian}')

hasil_pangkat = Bab_54a_module1.pangkat(6)
print(f'Hasil pangkat 6 dari 4 adalah = {hasil_pangkat(4)}\n')



# dgn cara from 
from Bab_54a_module1 import tambah,kali,pangkat
# from Bab_54a_module1 import *     --> otomatis import semua expression di dalam module (TIDAK DISARANKAN MEMAKAI INI. PAKE YG ATAS AJA)

hasil_pertambahan = tambah(1,2,3,4,5,6,7,8,9,10)  # hanya perlu panggil expression yg di dalam module saja
print(f'Hasil pertambahan = {hasil_pertambahan}')

hasil_perkalian = kali(1,2,3,4,5,6,7,8)
print(f'Hasil perkalian = {hasil_perkalian}')

hasil_pangkat = pangkat(10)
print(f'Hasil pangkat 10 dari 2 = {hasil_pangkat(2)}\n')



# ALIAS (as)

# cara import
import Bab_54a_module1 as module1

hasil_pertambahan = module1.tambah(1,2,3,4,5,6)
print(f'Hasil pertambahan = {hasil_pertambahan}')

hasil_perkalian = module1.kali(1,2,3,4)
print(f'Hasil perkalian = {hasil_perkalian}')

hasil_pangkat = module1.pangkat(7)
print(f'Hasil pangkat 7 dari 5 adalah = {hasil_pangkat(5)}\n')


# cara from (harus dipisah2 ketika akan meng-alias2 kan)
from Bab_54a_module1 import tambah as add
from Bab_54a_module1 import kali as times
from Bab_54a_module1 import pangkat as exponent

hasil_pertambahan = add(1,2,3,4,5,6,6,7,7,10)
print(f'Hasil pertambahan = {hasil_pertambahan}')

hasil_perkalian = times(1,2,3,4,4,3,2,1)
print(f'Hasil perkalian = {hasil_perkalian}')

hasil_pangkat = exponent(3)
print(f'Hasil pangkat 3 dari 12 adalah = {hasil_pangkat(12)}\n')
