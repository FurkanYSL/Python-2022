mükemmelsayılar = []

def mükemmel(sayı):
    toplam = 0
    for i in range(1,sayı):
        if(sayı % i == 0):
            toplam += i
            i +=1
        else:
            i+=1
    if(toplam==sayı):
        return toplam==sayı

for i in range(1,1001):
    if(mükemmel(i)==True):
        mükemmelsayılar.append(i)

print(mükemmelsayılar)