# memanggil file Gempa dan Import semua Method/Fungsi
from Gempa import *

# membuat objek Gempa dengan Argumen
gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gempa3 = Gempa('Cianjur', 5.6)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.0)

# informasi Gempa
print('## Info Gempa dong ra ##')
print()
gempa1.dampak()

# informasi Gempa
print('## Info Gempa dong ra ##')
print()
gempa2.dampak()

# informasi Gempa
print('## Info Gempa dong ra ##')
print()
gempa3.dampak()

# informasi Gempa
print('## Info Gempa dong ra ##')
print()
gempa4.dampak()

# informasi Gempa
print('## Info Gempa dong ra ##')
print()
gempa5.dampak()
