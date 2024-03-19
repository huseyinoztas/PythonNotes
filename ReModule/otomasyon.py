import re
import time

class Kayit:
    def __init__(self, programAd):
        self.programAd=programAd
        self.dongu=True

    def program(self):
        secim=self.menu()

        if secim=="1":
            print("kayit ekleme menüsüne yönlendiriliyorsunuz")
            time.sleep(3)
            self.kayitEkle()

        if secim=="2":
            print("kayit silme menüsüne yönlendiriliyorsunuz")
            time.sleep(3)
            self.kayitCikar()

        if secim=="3":
            print("Verilere erişiliyor")
            time.sleep(3)
            self.kayitOku()

        if secim=="4":
            self.cikis()
    
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-4]",secim):
                raise Exception("Lüften 1 ile 4 arasında geçerli bir seçim yapınız")
            elif len(secim)!=1:
                raise Exception("Lüften 1 ile 4 arasında geçerli bir seçim yapınız")
        while True:
            try:
                secim=input("Merhabalar, {} otomasyon sistemine hoşgeldiniz. \n\nLütfen yapmak istediğiniz işlemi seçiniz...\n\n[1] Kayıt ekle\n[2] Kayıt sil\n[3] Kayıt oku\n[4] Çıkış\n\n".format(self.program)) 
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim              


    def kayitEkle(self):
        def kontrolAd(Ad):
            if Ad.isalpha()==False:
                raise Exception("Adınız sadece alfabetik karakterlerden oluşmalıdır...")
        while True:
            try:
                Ad=input("Adınız: ")
                kontrolAd(Ad)
            except Exception as hataAd:
                print(hataAd)
                time.sleep(3)
            else:
                break

        
        def kontrolSoyAd(soyAd):
            if soyAd.isalpha()==False:
                raise Exception("Soyadınız sadece alfabetik karakterlerden oluşmalıdır...")
        while True:
            try:
                soyAd=input("Soyadınız: ")
                kontrolSoyAd(soyAd)
            except Exception as hataSoyAd:
                print(hataSoyAd)
                time.sleep(3)
            else:
                break


        def kontrolYas(yas):
            if yas.isdigit()==False:
                raise Exception("Yaşınız sadece rakamlardan oluşmalıdır...")
        while True:
            try:
                yas=input("Yaşınız: ")
                kontrolYas(yas)
            except Exception as hataYas:
                print(hataYas)
                time.sleep(3)
            else:
                break


        def kontrolTc(Tc):
            if Tc.isdigit()==False:
                raise Exception("Kimlik numaranız sadece rakamlardan oluşmalıdır...")
            elif len(Tc)!=11:
                raise Exception("Kimlik numaranız 11 rakamdan oluşmalıdır...")       
        while True:
            try:
                Tc=input("TC no: ")
                kontrolTc(Tc)
            except Exception as hataTc:
                print(hataTc)
                time.sleep(3)
            else:
                break

        def kontrolMail(Mail):
            if not re.search("@"and".com",Mail):
                raise Exception("Geçerli bir Mail adresi giriniz...")
        while True:
            try:
                Mail=input("Mail adresinizi giriniz: ")
                kontrolMail(Mail)
            except Exception as hataMail:
                print(hataMail)
                time.sleep(3)
            else:
                break
        with open("{YourPath}", "r", encoding="utf=8") as Dosya:
            satirSayisi=Dosya.readlines()
        if len(satirSayisi)==0:
            Id=1
        else:
            with open("{YourPath}", "r", encoding="utf=8") as Dosya:
                Id=int(Dosya.readlines()[-1].split("-")[0])+1
        with open("{YourPath}", "a+", encoding="utf=8") as Dosya:
            Dosya.write("{}-{} {} {} {} {}\n".format(Id,Ad,soyAd,yas,Tc,Mail))
            print("Veriler işlenmiştir.")
            self.menudon()

    def kayitCikar(self):
        y=input("Lüften silmek istediğiniz kişinin ID numarasını giriniz...")
        with open("{YourPath}", "r", encoding="utf=8") as Dosya:
            liste=[]
            liste2=Dosya.readlines()
            for i in range(0,len(liste2)):
                liste.append(liste2[i].split("-")[0])
        del liste2[liste.index(y)]

        with open("{YourPath}", "w+", encoding="utf=8") as yeniDosya:
            for i in liste2:
                yeniDosya.write(i)
        print("Kayıt siliniyor")
        time.sleep(3)
        print("Kayıt başarı ile silinmiştir")
        self.menudon()

    def kayitOku(self):
        with open("{YourPath}", "r", encoding="utf=8") as Dosya:
            for i in Dosya:
                print(i)
        self.menudon()
    def cikis(self):
        print("Otomasyondan çıkılıyor. Teşekkürler...")
        time.sleep(3)
        self.dongu=False
        exit()
    def menudon(self):
        while True:
            x=input("Ana menüye dönmek için 6 ya çıkmak için lüften 5 e basınız.")
            if x=="6":
                print("Ana menüye dönülüyor...")
                time.sleep(3)
                self.program()
                break
            elif x=="5":
                self.cikis()
                break
            else:
                print("Lütfen geçerli bir seçim yapınız...")








Sistem=Kayit("Anlasilir Ekonomi")

while Sistem.dongu:
    Sistem.program()