print("""***********
KULLANICI GİRİŞİ
**********""")
sys_username="furkanysl"
sys_password="123456"

username = input("Kullanıcı Adınızı Giriniz : ")
password = input("Parolanızı Gİriniz : ")

if  username==sys_username and password == sys_password:
    print("Giriş Başarılı")
elif username ==sys_username and password != sys_password:
    print("Parola Hatalı")
elif username !=sys_username and password == sys_password:
    print("Kullanıcı Adı Hatalı")
else:
    print("!!!Kullanıcı Adı ve Parola Hatalı!!!")