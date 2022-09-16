s1= int(input("Birinci Sayıyı Giriniz : "))
s2= int(input("İkinci Sayıyı Giriniz : "))
s3= int(input("Üçüncü Sayıyı Giriniz : "))

if s1>s2>s3:
    print(s1)
elif s1>s3>s2:
    print(s1)
elif s1>s2==s3:
    print(s1)
elif s1==s2>s3:
    print(s1)
elif s1==s3>s2:
    print(s1)
elif s2>s1>s3:
    print(s2)
elif s2>s3>s1:
    print(s2)
elif s2>s1==s3:
    print(s2)
elif s2==s1>s3:
    print(s2)
elif s2==s3>s1:
    print(s2)
elif s3>s2>s1:
    print(s3)
elif s3>s1>s2:
    print(s3)
elif s3>s1==s2:
    print(s3)
elif s3==s1>s2:
    print(s3)
elif s3==s2>s1:
    print(s3)