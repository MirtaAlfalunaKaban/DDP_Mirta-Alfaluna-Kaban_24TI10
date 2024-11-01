kendaraan = ['beat karbu',
'motor', '200', 'pink', 2]

kendaraan.append('13jt')
kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))


hitung_luas = int(input("""Pilih salah satu:
1.Hitung luas persegi
2.Hitung luas lingkaran)
3.Hitung luas segitiga
"""))

match hitung_luas:
    case 1:
        print('Menghitung luas persegi')
        sisi = int(input('Masukan nilai sisi: '))
        hitung_luas_persegi = sisi**2
        print(f"luas persegi dengan sisi {sisi} adalah {hitung_luas_persegi} cm^2")
    
    case _:
        print('pilihan tidak valid')


hitung_luas = int(input("""pilih salah satu:
1.hitung luas persegi
2.hitung luas lingkaran
3.hitung luas segitiga"""))

match hitung_luas:
  case 2:
     print('menghitung luas lingkaran')
     r = float(input('masukan nilai jari-jari: '))
     phi = 3.14
     hitung_luas_lingkaran = 2*r*r
     print('\nluasnya=',str("%.2f" % hitung_luas_lingkaran))
  case _:
     print('pilih tidak valid')

hitung_luas = int(input("""pilih salah satu:
1.hitung luas persegi
2.hitung luas lingkaran
3.hitung luas segitiga"""))

match hitung_luas:
  case 3:
     print('menghitung luas segitiga')
     alas = float(input('masukan nilai alas: '))
     tinggi = float(input('masukan nilai tinggi: '))
     hitung_luas_segitiga = 0.5*alas*tinggi
     print('\nluasnya=',str(hitung_luas_segitiga))
  case _:
     print('pilihan tidak valid')

