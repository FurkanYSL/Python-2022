print("""****************
1 ---> BAKİYE SORGULAMA
2 ---> PARA YATIRMA
3 ---> PARA ÇEKME
4 ---> ÇIKIŞ 
5 ---> GÜNLÜK ÇEKİM LİMİTİ ÖĞRENME
****************""")

sys_password = "123456"

bakiye = 5000
çekim_limiti = 2500

giriş_hakkı = 3
giriş_başarılı = 0

while (giriş_hakkı != 0):
    password = input("Parolanızı Gİriniz : ")
    if password != sys_password:
        print("Parola Hatalı!")
        giriş_başarılı = 2
        giriş_hakkı -= 1
    else:
        print("Giriş Başarılı!")
        giriş_başarılı = 1
        while (giriş_başarılı==1):
            işlem = int(input("Bir işlem seçiniz : "))
            if (işlem == 1):
                print("Bakiyeniz : {} ".format(bakiye))
                continue
            elif (işlem == 2):
                miktar = int(input("Yatırmak İstediğiniz Miktarı Giriniz : "))
                bakiye += miktar
                print("Paranız Yatırılmıştır")
                continue
            elif (işlem == 3):
                miktar = int(input("Çekmek İstediğiniz Miktarı Giriniz : "))
                if (bakiye >= miktar):
                    if (miktar <= çekim_limiti):
                        bakiye -= miktar
                        print("Paranız Verilmiştir")
                        continue
                    else:
                        print("Çekim Limitinden Fazla Miktarı Çekemzsiniz!")
                        continue
                else:
                    print("Girmiş Olduğumuz Miktarı Çekemzsiniz")
                    continue
            elif (işlem == 4):
                print("Bizi Tercih Ettiğniz İçin Teşekkür Eder Yine Bekleriz :)")
                giriş_başarılı = 0
            elif (işlem == 5):
                print("Günlük Çekim Limitiniz : {} ".format(çekim_limiti))
                continue
            else:
                print("YANLIŞ İŞLEM!")
                continue
    if(giriş_başarılı==0):
        break
    if (giriş_hakkı == 0):
        print("Giriş Hakkınız Kalmadı!!!")
        break