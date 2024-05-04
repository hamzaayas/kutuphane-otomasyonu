from admin import Admin
from uye import Uye
from kitap import Kitap
from misafir import  Misafir

# Örnek admin
admin = Admin(ad='admin', sifre="123")

# Örnek üye
uye = Uye(numara=200, sifre="uye")

#Örnek Misafir
misafir = Misafir()


# Örnek kitaplar
kitaplar = [
    Kitap(1, "Roman", "Kürk Mantolu Madonna", "Sabahattin Ali"),
    Kitap(2, "Roman", "Simyacı", "Paulo Coelho"),
    Kitap(4, "Roman", "Sineklerin Tanrısı", "William Golding"),
    Kitap(6, "Roman", "Tutunamayanlar", "Oğuz Atay"),
    Kitap(5, "Klasik", "Sefiller", "Victor Hugo"),
    Kitap(7, "Fantastik", "Harry Potter ve Felsefe Taşı", "J.K. Rowling"),
    Kitap(8, "Fantastik", "Yüzüklerin Efendisi", "J.R.R. Tolkien"),
]
