from random import randint
şifre=list()
while True:
    şifre_oluştur=randint(1,10)# rastgele sayı oluşturuyor
    şifre.append(şifre_oluştur)# sayıyı listeye ekliyor
    # aşağıda kontrol kodları var
    if len(şifre)<9:
        continue
    else:
        break
print(şifre)
print(f" şifreniz {şifre} olsun mu?")
