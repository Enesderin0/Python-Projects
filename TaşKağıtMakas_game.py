from random import choice 
degerler=["TAŞ","KAĞIT","MAKAS"] 


while True:
        try:
            kullanıcı = str(input("Taş mı? Kağıt mı? Makas mı? => "))
            kullanıcı=kullanıcı.upper()
            bilgisayar = choice(degerler)
        except NameError as açıklama:
            print("hata oluştu",açıklama)
            print("tekrar başlatılıyor")
            continue
    
        if kullanıcı == "TAŞ":
            if bilgisayar == "TAŞ":
                print("BERABERE")
            elif bilgisayar == "KAĞIT":
                print("BİLGİSAYAR KAZANDI")
            elif bilgisayar == "MAKAS":
                print("KAZANDINIZ")
        elif kullanıcı == "KAĞIT":
            if bilgisayar == "KAĞIT": 
                print("BERABERE")
            elif bilgisayar == "TAŞ":
                    print("KAZANDINIZ")
            elif bilgisayar == "MAKAS":
                print("BİLGİSAYAR KAZANDI")
        elif kullanıcı == "MAKAS":
            if bilgisayar == "MAKAS":
                print("BERABERE")
            elif bilgisayar == "KAĞIT":
                print("KAZANDINIZ")
            elif bilgisayar == "TAŞ":
                print("BİLGİSAYAR KAZANDI") 
            else:
                print("Yanlış Seçim Yaptınız")
                
                karar="oyuna decvam etmek ister misinz? Evet için 1 , Hayır için 2'yi tuşlayınız..."
                print(karar)
                karar=input(karar)
            
        if karar=="1":
            print("O Halde İşe Koyul Kaptan Ve Yapay Zekanın Canını Oku")
            continue
        
            
       
                    
                        