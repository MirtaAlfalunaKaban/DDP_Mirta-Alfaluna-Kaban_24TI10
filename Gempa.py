class Gempa:
    # konstruktor inisialisai atribut lokasi dan skala
    def __init__(self, lokasi, skala):

        # atribut
        self.lokasi = lokasi
        self.skala = skala

    # method menetukan dampak skala gempa
    def dampak(self):

        # statement / logika
        if self.skala < 2:
            print('Dampak Gempa Tidak Berasa')
        elif self.skala >=2 and self.skala <= 4:
            print('Dampak Gempa Bangunan Retak-retak')
        elif self.skala > 4 and self.skala <= 6:
            print('Dampak Gempa Bangunan roboh')
        elif self.skala > 6:
            print('Dampak Gempa Berpotensi Tsunami')

        # menampilkan Lokasi dan skala 
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')