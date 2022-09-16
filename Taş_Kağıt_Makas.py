import random
import time

tkm = ["Taş","Kağıt","Makas"]

rastgele_tkm = random.choice(tkm)

taş_kağıt_makas = input("Taş mı Kağıt mı Makas mı : ")

if(rastgele_tkm=="Taş"):
    if(taş_kağıt_makas=="Taş"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Taş = Taş Berabere")
    elif(taş_kağıt_makas=="Makas"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Taş Makası Kırar Kazanan Bilgisayar")
    elif(taş_kağıt_makas=="Kağıt"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Kağıt Taşı Sarar Kazanan Oyuncu")
    else:
        print("Geçersiz Oyun")

elif(rastgele_tkm=="Makas"):
    if (taş_kağıt_makas == "Taş"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Taş Makası Kırar Kazanan Oyuncu")
    elif (taş_kağıt_makas == "Makas"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Makas = Makas Berabere")
    elif (taş_kağıt_makas == "Kağıt"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Makas Kağıdı Keser Kazanan Bilgisayar")
    else:
        print("Geçersiz Oyun")

elif(rastgele_tkm=="Kağıt"):
    if (taş_kağıt_makas == "Taş"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Kağıt Taşı Sarar Kazanan Bilgisayar")
    elif (taş_kağıt_makas == "Makas"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Makas Kağıdı Keser Kazanan Oyuncu")
    elif (taş_kağıt_makas == "Kağıt"):
        time.sleep(1)
        print("Bilgisayarın Seçimi : {}".format(rastgele_tkm))
        print("Kağıt = Kağıt Berabere")
    else:
        print("Geçersiz Oyun")

else:
        print("Geçersiz Oyun")