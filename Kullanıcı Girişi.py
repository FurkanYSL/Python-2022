sys_username = "furkanysl"
sys_password = "123456"

giriş_hakkı = 3

while (giriş_hakkı != 0):
    username = input("Kullanıcı Adınızı Giriniz : ")
    password = input("Parolanızı Gİriniz : ")
    if username != sys_username and password != sys_password:
        print("Parola ve Kullanıcı Adı Hatalı!")
        giriş_hakkı -= 1
    elif username == sys_username and password != sys_password:
        print("Parola Hatalı!")
        giriş_hakkı -= 1
    elif username != sys_username and password == sys_password:
        print("Kullanıcı Adı Hatalı!")
        giriş_hakkı -= 1
    else:
        print("Giriş Başarılı!")
        break
    if (giriş_hakkı == 0):
        print("Giriş Hakkınız Kalmadı!!!")

