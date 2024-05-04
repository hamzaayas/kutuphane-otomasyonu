from ornekVeriler import admin, uye, misafir, kitaplar

def giris_yap():
    while True:
        secim = input("1. Admin girişi\n2. Üye girişi\n3. Misafir girişi\n4. Sistemden Çıkma\nSeçiminiz: ")


        #Admin İşlemleri

        if secim == "1":
            print("1'e basarak Admin Giriş Seçeneğini Seçtiniz ")
            loginNumara = (input("Admin Nickname: "))
            loginSifre = input("Şifre: ")

            if loginNumara == admin.ad and loginSifre == admin.sifre:
                print("Admin girişi başarılı\n")

                while True:
                    secimAdmin = input("KE. Kitap Ekle\nKG. Kitap Güncelleme\nKS. Kitap Silme\nAMD. Ana Menüye Dön\nSeçiminiz: ")

                    if secimAdmin == "KE" or secimAdmin == "ke":
                        admin.kitap_ekle()
                        yildizEkle() # Her ifade için print yazmak yerine 1 kere fonksiyon oluşturuldu ve her ifade de çağrıldı


                    elif secimAdmin == "KG" or secimAdmin == "kg":
                        admin.kitap_guncelle()
                        yildizEkle()


                    elif secimAdmin == "KS" or secimAdmin == "ks":
                        admin.kitap_sil()
                        yildizEkle()

                    elif secimAdmin == "AMD" or secimAdmin == "amd":
                        break

                    else:
                        print("Doğru seçeneklerden birini giriniz!\n")

            else:
                print("Yanlış admin numarası veya şifre")



        #Üye İşlemleri

        elif secim == "2":
            print("2'ye basarak Üye Giriş Seçeneğini Seçtiniz ")
            loginNumara = int(input("Üye numarası: "))
            loginSifre = input("Şifre: ")

            if loginNumara == uye.numara and loginSifre == uye.sifre:
                print("Üye girişi başarılı\n")

            while True:
                secimUye = input("RY. Rezervasyon Yap\nKA. Kitap Arama\nKOA. Kitap Ödünç Alma\nAMD. Ana Menüye Dön\nSeçiminiz: ")

                if secimUye == "RY" or secimUye == "ry":
                    uye.rezervasyon_yap()
                    yildizEkle()  # Her ifade için print yazmak yerine 1 kere fonksiyon oluşturuldu ve her ifade de çağrıldı


                elif secimUye == "KA" or secimUye == "ka":
                    uye.kitap_ara()
                    yildizEkle()

                    print("İstediğiniz kitap türünü seçiniz\n")

                    secimKitapTuru = input("R. Roman\nF. Fantastik\nK. Klasik\nSeçiminiz: ")

                    if secimKitapTuru == "R" or secimKitapTuru == "r":

                        for kitap in kitaplar:
                            if kitap.kitap_turu == "Roman":
                                print(kitap)



                    elif secimKitapTuru == "F" or secimKitapTuru == "f":

                        for kitap in kitaplar:
                            if kitap.kitap_turu == "Fantastik":
                                print(kitap)


                    elif secimKitapTuru == "K" or secimKitapTuru == "k":

                        for kitap in kitaplar:
                            if kitap.kitap_turu == "Klasik":
                                print(kitap)

                    else:
                        print("Doğru seçeneklerden birini giriniz!\n")

                    yildizEkle()



                elif secimUye == "KOA" or secimUye == "koa":
                    uye.kitap_odunc_al()
                    yildizEkle()


                elif secimUye == "AMD" or secimUye == "amd":
                    break

                else:
                    print("Doğru seçeneklerden birini giriniz!\n")


            else:
                print("Yanlış üye numarası veya şifre\n")


        if secim == "3":
            print("Misafir Girişi Başarılı \n")
            misafir.kitap_ara()

            for kitap in kitaplar:
                print(kitap)

            yildizEkle()


        if secim == "4": # Ana Menüdeki Programdan Çıkma Seçeneği
            print("Programdan çıkılıyor")
            break


def yildizEkle():
    print('*****************\n')

girisYap = giris_yap()
