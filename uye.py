# Üye sınıfı
class Uye:
    def __init__(self, numara, sifre):
        # Üyenin  numara ve şifre alanları
        self.numara = numara
        self.sifre = sifre

    def rezervasyon_yap(self):
        # Rezervasyon yapma fonksiyonu
        print("Rezervasyon yapıldı")

    def kitap_ara(self):
        # Kitap arama fonksiyonu
        print("Kitap arandı")

    def kitap_odunc_al(self):
        # Kitap ödünç alma fonksiyonu
        print("Kitap ödünç alındı")
