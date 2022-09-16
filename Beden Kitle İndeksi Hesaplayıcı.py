print("BEDEN KİTLE İNDEKSİ HESAPLAYICI")
boy = float(input("Boyunuzu m cinsinden girinz : "))
kilo = float(input("Kilonuzu kg cinsinden giriniz : "))

print("Boyunuz : ",boy)
print("Kilonuz : ",kilo)

beden_kitle_indeksi = kilo / (boy * boy)
print(beden_kitle_indeksi)

if beden_kitle_indeksi<18.5:
    print("ZAYIF!")
elif beden_kitle_indeksi >18.5 and beden_kitle_indeksi<25:
    print("NORMAL")
elif beden_kitle_indeksi >25 and beden_kitle_indeksi <30:
    print("FAZLA KİLOLU!")
else:
    print("!!!OBEZ!!!")