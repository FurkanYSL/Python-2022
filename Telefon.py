import time
class telefon():
    def __init__(self,marka,model,ram,hafıza,arka_kamera,ön_kamera,durum = "Kapalı",ses_seviyesi = 0,uygulama_listesi = [],uygulama_sayısı=0,wifi_durum = "Kapalı",bluetooth_durum = "Kapalı"):
        self.marka = marka
        self.model = model
        self.hafıza = hafıza
        self.ram = ram
        self.arka_kamera = arka_kamera
        self.ön_kamera = ön_kamera
        self.durum = durum
        self.ses_seviyesi = ses_seviyesi
        self.uygulama_sayısı = uygulama_sayısı
        self.uygulama_listesi = uygulama_listesi
        self.wifi_durum = wifi_durum
        self.bluetooth_durum = bluetooth_durum

    def aç(self):
        if (self.durum == "Açık"):
            print("Telefon Zaten Açık")
            time.sleep(1)
        else:
            gir = input("Telefonu Açmak için 'e' ye basınız ")
            if (gir == "e"):
                print("Telefon Açılıyor")
                time.sleep(2)
                self.durum = "Açık"
                print("Telefon Açıldı")
                time.sleep(1)
            else:
                print("Hatalı Giriş")

    def kapat(self):
        if (self.durum == "Kapalı"):
            print("Telefon Zaten Kapalı")
            time.sleep(1)
        else:
            gir2 = input("Telefonu Kapatmak için 'q' ya basınız ")
            if (gir2 == "q"):
                print("Telefon Kapatılıyor")
                time.sleep(2)
                self.durum = "Kapalı"
                print("Telefon Kapatıldı")
                time.sleep(1)
            else:
                print("Geçersiz İşlem")

    def telefon_bilgileri(self):
        print("Marka : {}\nModel : {}\nRam : {}\nHafıza : {} GB\nArka Kamera {} MP\nÖn Kamera : {} MP\nUygulama Sayısı : {}\nDurum : {}\nSes Seviyesi : {}\nUygulama Listesi : {}\nWi-Fi Durum : {}\nBluetooth Durum : {}\n".format(self.marka,self.model,self.ram,self.hafıza,self.arka_kamera,self.ön_kamera,self.uygulama_sayısı,self.durum,self.ses_seviyesi,self.uygulama_listesi,self.wifi_durum,self.bluetooth_durum))
        time.sleep(3)

    def ses_aç(self):
        if (self.durum == "Açık"):
            while True:
                giriş = input(print("Sesi Artırmak İçin '+' ya basınız :\nÇıkmak İçin q ya Basınız : "))
                if(giriş=="+"):
                    if(self.ses_seviyesi==100):
                        print("Ses Son Seviyede")
                    elif(self.ses_seviyesi!=100):
                        print("Ses Artırılıyor")
                        self.ses_seviyesi += 5
                    else:
                        print("Hatalı Giriş")
                elif(giriş == "q"):
                    break
                else:
                    print("Hatalı Giriş")
        else:
            print("Telefon Kapalıyken Ses Artırılamaz")
            time.sleep(1)

    def ses_kapa(self):
        if (self.durum == "Açık"):
            while True:
                giriş2 = input(print("Sesi Azaltmak İçin '-' ya basınız : \nÇıkmak İçin q ya Basınız : "))
                if (giriş2 == "-"):
                    if (self.ses_seviyesi == 0):
                        print("Ses Daha Fazla Azaltılamaz")
                    elif (self.ses_seviyesi != 0):
                        print("Ses Azaltılıyor")
                        self.ses_seviyesi -= 5
                    else:
                        print("Hatalı Giriş")
                elif (giriş2 == "q"):
                    break
                else:
                    print("Hatalı Giriş")
        else:
            print("Telefon Kapalıyken Ses Kısılamaz")
            time.sleep(1)

    def wifi_aç(self):
        if (self.durum == "Açık"):
            if (self.wifi_durum == "Kapalı"):
                giriş3 = input("Wi-Fi yi açmak için 'e' ye basın : ")
                if (giriş3 == "e"):
                    print("Wifi Açılıyor")
                    self.wifi_durum = "Açık"
                    time.sleep(1)
                    print("Wi-Fi Açıldı")
                    time.sleep(2)
                else:
                    print("Hatalı İşlem")
            else:
                print("Wi-Fi Zaten Açık")
                time.sleep(1)
        else:
            print("Telefon Kapalıyken Wi-Fi Açılamaz")
            time.sleep(1)

    def wifi_kapat(self):
        if (self.durum == "Açık"):
            if (self.wifi_durum == "Açık"):
                giriş4 = input("Wi-Fi yi kapatmak için 'q' ya basınız : ")
                if (giriş4 == "q"):
                    print("Wifi Kapatılıyor")
                    self.wifi_durum = "Kapalı"
                    time.sleep(1)
                    print("Wi-Fi Kapatıldı")
                    time.sleep(2)
                else:
                    print("Hatalı İşlem")
            else:
                print("Wi-Fi Zaten Kapalı")
                time.sleep(1)
        else:
            print("Telefon Kapalıyken Wi-Fi Kapatılamaz")
            time.sleep(1)

    def bluetooth_aç(self):
        if(self.durum=="Açık"):
            if (self.bluetooth_durum == "Kapalı"):
                giriş5 = input("Bluetooth açmak için 'e' ye basın")
                if (giriş5 == "e"):
                    print("Bluetooth Açılıyor")
                    self.bluetooth_durum = "Açık"
                    time.sleep(1)
                    print("Bluetooth Açıldı")
                    time.sleep(2)
                else:
                    print("Hatalı İşlem")
            else:
                print("Bluetooth Zaten Açık")
                time.sleep(1)
        else:
            print("Telefon Kapalıyken Bluetooth Açılamaz")
            time.sleep(1)

    def bluetooth_kapat(self):
        if (self.durum == "Açık"):
            if (self.bluetooth_durum == "Açık"):
                giriş6 = input("Bluetooth kapatmak için 'q' ya basın")
                if (giriş6 == "q"):
                    print("Bluetooth Kapatılıyor")
                    self.bluetooth_durum = "Kapalı"
                    time.sleep(1)
                    print("Bluetooth Kapatıldı")
                    time.sleep(2)
                else:
                    print("Hatalı İşlem")
            else:
                print("Bluetooth Zaten Kapalı")
                time.sleep(1)
        else:
            print("Telefon Kapalıyken Bluetooth Kapatılamaz ")
            time.sleep(1)

    def uygulama_ekle(self,uyg_ismi):
        if (self.durum == "Açık"):
            print("Uygulama İndiriliyor.....")
            time.sleep(5)
            self.uygulama_listesi.append(uyg_ismi)
            print("Uygulama Yüklendi\nYüklenen Uygulama {}".format(uyg_ismi))
            time.sleep(2)
        else:
            print("Telefon Kapalıyken Uygulama Yüklenemez")
            time.sleep(1)

    def __len__(self):
        return len(self.uygulama_listesi)

    def __str__(self):
        return "Marka : {}\nModel : {}\nRam : {}\nHafıza : {} GB\nArka Kamera {} MP\nÖn Kamera : {} MP\nUygulama Sayısı : {}\nSes Seviyesi : {}\nUygulama Listesi : {}\nWi-Fi Durum : {}\nBluetooth Durum : {}\n"

telefon = telefon("İphone","X","4","64","8","4")

while True:
    işlem = input("İşlem 1 : Telefon Aç\nİşlem 2 : Telefon Kapat\nİşlem 3 : Telefon Bilgilerini Göster\nİşlem 4 : Ses Aç\nİşlem 5 : Ses Azalt\nİşlem 6 : Wi-Fi Aç\nİşlem 7 : Wi-Fi Kapat\nİşlem 8 : Bluetooth Aç\nİşlem 9 : Bluetooth Kapat\nİşlem 10 : Uygulama Ekle\nİşlem 11 : Çıkış Yap\nBir İşlem Seçiniz : ")

    if(işlem == "11"):
        print("İşlem Sonlandırılıyor")
        break
    elif(işlem == "1"):
        telefon.aç()
    elif(işlem == "2"):
        telefon.kapat()
    elif(işlem == "3"):
        telefon.telefon_bilgileri()
    elif(işlem == "4"):
        telefon.ses_aç()
    elif(işlem == "5"):
        telefon.ses_kapa()
    elif(işlem == "6"):
        telefon.wifi_aç()
    elif(işlem == "7"):
        telefon.wifi_kapat()
    elif(işlem == "8"):
        telefon.bluetooth_aç()
    elif(işlem == "9"):
        telefon.bluetooth_kapat()
    elif(işlem == "10"):
        uygulama_isimleri = input("Eklemek İstediğiniz Uygulamaları ',' ile AYIRARAK Yazınız : ")
        uygulama_listesi = uygulama_isimleri.split(",")
        for eklenecek_uygulamalar in uygulama_listesi:
            telefon.uygulama_ekle(eklenecek_uygulamalar)
            telefon.uygulama_sayısı += 1
    else:
        print("Hatalı İşlem Seçildi...")


