# Admin sınıfı
class Admin:
    def __init__(self, ad, sifre):
        # Adminin  numara ve şifre alanları
        self.ad = ad
        self.sifre = sifre

    def kitap_ekle(self):
        # Kitap ekleme fonksiyonu
        print("Kitap eklendi")

    def kitap_guncelle(self):
        # Kitap güncelleme fonksiyonu
        print("Kitap güncellendi")

    def kitap_sil(self):
        # Kitap silme fonksiyonu
        print("Kitap silindi")
