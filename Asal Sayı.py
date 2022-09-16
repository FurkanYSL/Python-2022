def asalsayı(sayı):
    if sayı>2:
        for i in range(2,sayı):
            if (sayı%i==0):
                return False
            return True
    elif (sayı==2):
        return True
    else:
        return False

while True:
    sayı = input("Bir Sayı Giriniz(Çıkmak İçin q ya Basınız) : ")
    if sayı == "q":
        break
    else:
        sayı = int(sayı)
        if(asalsayı(sayı)==True):
            print(sayı,"Sayısı Asaldır")
        else:
            print(sayı,"Sayısı Asal Sayı Değildir")

