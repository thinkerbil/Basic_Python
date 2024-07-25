# IMPORT STATEMENT (import statement dari file lain)
# berguna jika statement nya panjang banget  --> dgn cara import statement ke file baru (file utama), maka dapat menyederhanakan program

import os
os.system('cls')


# Contoh 1: Meng-inport Bentuk PRINT   --> pada file utama, kita hanya import saja, tidak perlu di-print
# Buat file baru dgn nama: 'bab53a_import_print_nama'  --> isi file nya bukan variabel
import bab_53a_import_print_nama

# Buat file baru dgn nama: 'bab53a_import_print_angka'  --> isi file nya bukan variable data
import bab_53a_import_print_angka


# Contoh 2:  Meng-import Variable Data pada File lain    --> format:  namafile.namavar
# Buat file baru dgn nama: 'bab_53b_import_nama'  --> isi file nya adalah variabel. ada 2 variabel pada file tsb
import bab_53b_import_nama
print(f'Nama: {bab_53b_import_nama.nama_1}')
print(f'Nama: {bab_53b_import_nama.nama_2}')












