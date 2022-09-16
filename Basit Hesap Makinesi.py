print("1 : Toplama // 2 : Çıkartma // 3 : Çarpma // 4 : Bölme // 5 : Kalan Bulma // 6 : Üssünü Alma")

islem = int(input("Bir İşlem Seçiniz : "))

if  islem==1:
    print("Toplama İşlemi Seçildi")
elif  islem==2:
    print("Çıkartma İşlemi Seçildi")
elif  islem==3:
    print("Çarpma İşlemi Seçildi")
elif  islem==4:
    print("Bölme İşlemi Seçildi")
elif  islem==5:
    print("Kalan Bulma Seçildi")
elif  islem==6:
    print("Üssünü Alma Seçildi")
else:
    print("Hatalı İşlem Girildi!")

sayi1 = float(input("1. Sayıyı Giriniz : "))
sayi2 = float(input("2. Sayıyı Giriniz : "))

if islem == 1:
    print("Sonuç : {}".format(sayi1+sayi2))
elif islem ==2:
    print("Sonuç : {}".format(sayi1-sayi2))
elif islem==3:
    print("Sonuç : {}".format(sayi1*sayi2))
elif islem ==4:
    print("Sonuç : {}".format(sayi1/sayi2))
elif islem ==5:
    print("Sonuç : {}".format(sayi1 % sayi2))
elif islem ==6:
    print("Sonuç : {}".format(sayi1**sayi2))
else:
    print("Hatalı İşlem!")

