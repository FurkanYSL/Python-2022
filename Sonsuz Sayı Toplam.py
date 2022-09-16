print("**********ÇIKMAAK İÇİN q ya BASINIZ**********")

toplam = 0

while True:
    sayı = (input("Bir Sayı Giriniz : "))
    if(sayı != "q"):
        sayı = int(sayı)
        toplam += sayı
        continue
    else:
        print("Program Sonlandırılmıştır!")
        print("Girdiğiniz Sayıların Toplamı : {} ".format(toplam))
        break


