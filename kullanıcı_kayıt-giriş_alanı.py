"""
kullanıcının kayıt alanı
        kullanıcı adı 
        şifre
        şifre kontrol
        güvenlik kodu
kullanıcı giriş alanı
        kullanıcı adı kontrol
        şifre kontrol
"""
güvenlik_kodu="QW135790"
while True:
    
    name=input("Adınızı Giriniz: ")
    name=name.upper()
    kayıt_kullanıcı_adı=input("Kullanıcı Adı Oluşturunuz: ")
    kayıt_şifre=input("Şifre Oluşturunuz: ")
    kayıt_şifre_kontrol=input("Şifrenizi Tekrar Giriniz: ")
    if kayıt_şifre!=kayıt_şifre_kontrol:
        print("\nŞifreler Uyuşmuyor\nTekrar Kayıt Ekranına Dönülüyor..")
        continue
    kayıt_güvenlik_kodu=input("Gönderilen Güvenlik Kodunu Giriniz: ")
    if kayıt_güvenlik_kodu!=güvenlik_kodu:
        print("\nGüvenlik Kodunu Yanlış Girdiniz\nKayıt Ekranına Tekrar Dönülüyor..")
        continue
    print("\nHoşgeldiniz ",name)
    break
    
while True:
    giriş_kullanıcı_adı=input("Kullanıcı Adınızı Giriniz: ")
    if giriş_kullanıcı_adı!=kayıt_kullanıcı_adı:
        print("Yanlış kullanıcı Adı Girdiniz")
        print("Giriş Ekranına Dönülüyor")
        continue
    giriş_şifre=input("Şifrenizi Giriniz: ")
    if giriş_şifre!=kayıt_şifre:
        print("Yanlış Şifre Girdiniz")
        print("Giriş Ekranına Dönülüyor")
    if giriş_kullanıcı_adı==kayıt_kullanıcı_adı and giriş_şifre==kayıt_şifre:
        print("Hoşgeldin ",name)
        break
    else:
        print("Sistemde Hata Oluştu")
        print("Giriş Ekranına Dönülüyor")
        continue

print("Çıkış Yapmak İsterseniz X tuşuna basınız")
karar=input("Kararınız: ")
if (karar=="x")or(karar=="X"):
    print("Çok Özletme Kendini ",name)
    