sayı1 = int(input("Birinci Sayıyı Giriniz : "))
sayı2 = int(input("İkinci Sayıyı Giriniz : "))

def ebob(sayı1,sayı2):
    if (sayı1>=sayı2):
        ebob = 1
        for i in range(1,sayı2+1):
            if(sayı1%i==0 and sayı2%i==0):
                ebob = i
    else:
        for i in range(1,sayı1+1):
            if (sayı1 % i == 0 and sayı2 % i == 0):
                ebob = i

    return ebob

def ekok(sayı1,sayı2):
    return ((sayı1*sayı2) // ebob(sayı1,sayı2))

print(ekok(sayı1,sayı2))