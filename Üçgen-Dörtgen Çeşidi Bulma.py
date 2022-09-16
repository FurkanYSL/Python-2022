print("""1 : Üçgen Tip Bulucu
2 : Dörtgen Tip Bululcu """)

işlem = int(input("Bir işlem seçiniz : "))
if işlem==1:
    k1 = abs(float(input("1. Kenarı Giriniz : ")))
    k2 = abs(float(input("2. Kenarı Giriniz : ")))
    k3 = abs(float(input("3. Kenarı Giriniz : ")))
elif işlem==2:
    k1 = abs(float(input("1. Kenarı Giriniz : ")))
    k2 = abs(float(input("2. Kenarı Giriniz : ")))
    k3 = abs(float(input("3. Kenarı Giriniz : ")))
    k4 = abs(float(input("4. Kenarı Giriniz : ")))
else:
    print("Hatalı İşlem!")
if işlem==1:
    if k1==k2==k3:
        print("Kenarları Girilen Üçgen Eşkenar Üçgendir")
    elif k1==k2 and k1 != k3:
        print("Kenarları Girilen Üçgen İkizkenar Üçgendir")
    else:
        print("Kenarları Girilen Üçgen Çeşitkenar Üçgendir")
elif işlem==2:
    if k1==k2==k3==k4:
        print("Kenarları Girilen Dörtgen Karedir")
    elif (k1==k2 and k3==k4) or (k1==k3 and k2==k4) or (k1==k4 and k2==k3):
        print("Kenarları Girilen Dörtgen Dikdörtgendir")
    else:
        print("Kenarları Girilen Dörtgen Kare veya Dikdörtgen Değildir")