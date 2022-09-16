sayı = int(input("Bir Sayı Giriniz : "))
tambölenler = []

def tambölenbul(sayı):
    for i in range(sayı,0,-1):
        if(sayı%i==0):
            tambölenler.append(i)
    return tambölenler

print(tambölenbul(sayı))