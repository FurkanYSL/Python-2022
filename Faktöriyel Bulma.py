print("""****************
FAKTÖRİYEL HESAPLAYICI

Çıkmak İçin q ya Basınız
****************""")

while True:#Biz Programı Sonlandırana Kadar Döngünün Devam Etmesi İçin True Yazdık
    sayı = input("Bir Sayı Giriniz : ")

    if(sayı == "q"):
        print("Program Sonlandırılmıştır")
        break
    else:
        sayı = int(sayı)
        faktöriyel = 1
        for x in range(sayı,0,-1):
            faktöriyel *= x
    print("{} sayısının faktöriyeli : {}".format(sayı,faktöriyel))


