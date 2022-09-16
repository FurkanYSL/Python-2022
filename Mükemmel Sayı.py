sayı = int(input("Bir Sayı Giriniz : "))

toplam = 0

for i in range(sayı-1,0,-1):
    if(sayı%i==0):
        toplam += i
        i = i + 1
    else:
        i +=1
if(sayı==toplam):
    print("{} Sayısı Mükemmel Bir Sayıdır".format(sayı))
else:
    print("{} Sayısı Mükemmel Bir Sayı Değildir".format(sayı))