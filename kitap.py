# Kitap sınıfı,
class Kitap:
    def __init__(self, kitap_id, kitap_turu, kitap_adi, yazar):
        # Kitabın id
        self.kitap_id = kitap_id
        # Kitabın türü
        self.kitap_turu = kitap_turu
        # Kitabın adı
        self.kitap_adi = kitap_adi
        # Kitabın yazarı
        self.yazar = yazar

    def __str__(self):
        return f"Kitap ID: {self.kitap_id}, Türü: {self.kitap_turu}, Adı: {self.kitap_adi}, Yazar: {self.yazar}"
