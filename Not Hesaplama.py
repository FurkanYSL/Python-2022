vize1 = float(input("1. Vize Notunu Giriniz : "))
vize2 = float(input("2. Vize Notunu Giriniz : "))
final = float(input("Final Notunu Giriniz : "))

toplam_not = (vize1*0.3)+(vize2*0.3)+(final*0.4)

if  toplam_not >= 90:
    print(toplam_not)
    print("AA")
elif toplam_not >= 85:
    print(toplam_not)
    print("BA")
elif toplam_not >= 80:
    print(toplam_not)
    print("BB")
elif toplam_not >= 75:
    print(toplam_not)
    print("CB")
elif toplam_not >= 70:
    print(toplam_not)
    print("CC")
elif toplam_not >= 65:
    print(toplam_not)
    print("DC")
elif toplam_not >= 60:
    print(toplam_not)
    print("DD")
elif toplam_not >= 55:
    print(toplam_not)
    print("FD")
else:
    print(toplam_not)
    print("FF")