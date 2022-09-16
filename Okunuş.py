def okunuş():
    sayı = int(input("Bir sayı giriniz : "))

    birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

    if(0<sayı<100):
        return(onlar[sayı//10]+" "+birler[sayı%10])
    else:
        print("Sadece 2 Basamaklı Sayıları Giriniz!!!")

print(okunuş())