import math

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'Luas balok adalah {hitung}')

def l_kubus(rusuk):
    hitung = rusuk * rusuk 
    print(f'Luas kubus adalah {hitung}')

def l_limas(alas, tinggi):
    hitung = 1/3 * alas * tinggi
    print(f'luas limas adalah {hitung}')

def l_prisma(alas, tinggi):
    hitung = 1/2 * alas * tinggi
    print(f'hitung luas prisma {hitung}')

def l_tabung(alas, tinggi):
    hitung = alas * tinggi
    print(f'hitung luas tabung {hitung}')