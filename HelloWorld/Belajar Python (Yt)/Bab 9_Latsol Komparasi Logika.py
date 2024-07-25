# # example: +++++A------B+++++
# # Arti: (+) True, (-) False


# # RENTANG AREA: +++++++++3--------10+++++++++
# # Rentang area: Data kurang dari 3 ATAU data kurang dari 10
# print("RENTANG AREA: +++++++++3--------10+++++++++")
# data = int(input('Masukkan data yang nilainya kurang dari 3 ATAU lebih dari 10: '))

# # +++++++++3----------
# kurangdari = data < 3
# print(f"{data} < 3 = {kurangdari}")

# # ----------------10++++++++++
# lebihdari = data > 10
# print(f"{data} > 10 = {lebihdari}")

# # melihat hubungan dari data yang diambil terhadap rentang area, gunakan "or" karena daerah yang (+)/TRUE ada DUA
# hasil = kurangdari or lebihdari
# print(f"Kesimpulan: {kurangdari} or {lebihdari} = {hasil}")


# print()
# # RENTANG AREA: ---------3+++++++++++10---------
# # Rentang area: Data Lebih dari 3 DAN kurang dari 10 (Irisan)
# print("RENTANG AREA: ---------3+++++++++++10---------")
# data = int(input('Masukkan data yang nilainya lebih dari 3 DAN kurang dari 10: '))

# # ------3+++++++++++++
# lebihdari = data > 3
# print(f"{data} > 3 = {lebihdari}")

# # +++++++++++++++++++10-------------
# kurangdari = data < 10
# print(f'{data} < 10 = {kurangdari}')

# # Melihat hubungan dari data yang diambil terhadap rentang area, gunakan "AND" karena daerah (+)/TRUE di tengah2/irisan
# hasil = lebihdari and kurangdari
# print(f'Kesimpulan: {lebihdari} and {kurangdari} = {hasil}')



print()
# Soal 1
# Area: -------- 0 ++++++++ 5 -------- 8 ++++++++ 11 --------
print('Area: -----0+++++5------8++++++11------')
soal1 = int(input('Masukkan angka: '))
print()
hasil_1 = soal1 > 0
hasil_2 = soal1 < 5
hasil_3 = soal1 > 8
hasil_4 = soal1 < 11

print(f'{soal1} > 0 = {hasil_1}')
print(f'{soal1} < 5 = {hasil_2}')
print(f'{soal1} > 8 = {hasil_3}')
print(f'{soal1} < 11 = {hasil_4}')

kesimpulan = hasil_1 and hasil_2 or hasil_3 and hasil_4
print(f'Kesimpulan: {hasil_1} and {hasil_2} or {hasil_3} and {hasil_4} = {kesimpulan}')


print()
# Soal 2
# Area: +++++ 0 ----- 5 +++++ 8 ----- 11 +++++
print('Area: +++++0-----5+++++8-----11+++++')
soal2 = int(input('Masukkan angka: '))

hasil_1 = soal2 < 0
hasil_2 = soal2 > 5
hasil_3 = soal2 < 8
hasil_4 = soal2 > 11

print(f'{soal2} < 0 = {hasil_1}')
print(f'{soal2} > 5 = {hasil_2}')
print(f'{soal2} < 8 = {hasil_3}')
print(f'{soal2} > 11 = {hasil_4}')

kesimpulan = hasil_1 or hasil_2 and hasil_3 or hasil_4
print(f'Kesimpulan: {hasil_1} or {hasil_2} and {hasil_3} or {hasil_4} = {kesimpulan}')