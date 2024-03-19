import json
import re
import time
import random

class Site:
    def __init__(self):
        self.dongu=True
        self.veriler=self.veriAl()

    def program(self):
        secim=self.menu()

        if secim=="1":
            self.giris()
        if secim=="2":
            self.kayitOl()
        if secim=="3":
            self.cikis()

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-3]",secim):
                raise Exception("Lüften 1 ve 3 arasında bir seçim yapınız...")
            elif len(secim)!=1:
                raise Exception("Lüften 1 ve 3 arasında bir seçim yapınız...")
        while True:
            try:
                secim=input("Merhabalar hoş geldiniz.\n\nLüften yapmak istediğiniz işlemi seçiniz...\n\n[1] - Giriş\n[2] - Kayıt ol\n[3] - Çıkış\n\n ")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        return secim

    def giris(self):
        print("Giriş menüsüne yönlendiriliyorsunuz")
        time.sleep(2)
        kullaniciAdi=input("Lüften kullanıcı adınızı giriniz: ")
        sifre=input("Lüften şifrenizi giriniz: ")

        sonuc=self.girisKontrol(kullaniciAdi,sifre)


        if sonuc==True:
            self.girisBasarili()
        else:
            self.girisBasarisiz()

    def girisKontrol(self,kullaniciAdi,sifre):
        self.veriler=self.veriAl()
        try:
            for kullanici in self.veriler["Kullanıcılar"]:
                if kullanici["Kullanıcıadı"]==kullaniciAdi and kullanici["Sifre"]==sifre:
                    return True
        except KeyError:
            return False
        return False

    def girisBasarili(self):
        print("Kontrol ediliyor...")
        time.sleep(2)
        print("Giriş başarılı. Anlaşılır ekonomi sitesine hoşgeldiniz.")
        self.sonuc=False
        self.dongu=False

    def girisBasarisiz(self):
        print("Kullanıcı adı veya şifre hatalı!!!")
        time.sleep(2)
        self.menuDon()

    def kayitOl(self):
        def kontrolKa(kullaniciAdi):
            if len(kullaniciAdi)<8:
                raise Exception("Kullanıcı adınız en az 8 karakterden oluşmalıdır.")
        while True:
            try:
                kullaniciAdi=input("Kullanıcı Adınız: ")
                kontrolKa(kullaniciAdi)
            except Exception as hataAd:
                print(hataAd)
                time.sleep(2)
            else:
                break
        def kontrolSifre(sifre):
            if len(sifre)<8:
                raise Exception("Şifreniz en az 8 karakterden oluşmalıdır.")
            elif not re.search("[0-9]",sifre):
                raise Exception("Şifreniz en az 1 tane rakam olmalıdır")
            elif not re.search("[A-Z]",sifre):
                raise Exception("Şifreniz en az 1 tane büyük harf olmalıdır")
            elif not re.search("[a-z]",sifre):
                raise Exception("Şifreniz en az 1 tane küçük harf olmalıdır")
               
        while True:
            try:
                sifre=input("Şifreniz: ")
                kontrolSifre(sifre)
            except Exception as hataSifre:
                print(hataSifre)
                time.sleep(2)
            else:
                break
        
        def kontrolMail(mail):
            if not re.search("@" and ".com", mail):
                raise Exception("Geçerli bir mail adresi giriniz.")
        while True:
            try:
                mail=input("Mail adresiniz: ")
                kontrolMail(mail)
            except Exception as hataMail:
                print(hataMail)
                time.sleep(2)
            else:
                break
        sonuc=self.kayitVarmi(kullaniciAdi,mail)
        if sonuc==True:
            print("Bu kullanıcı adı ve mail sistemde kayıtlı")
        else:
            aktivasyonKodu=self.aktivasyonGonder()
            durum=self.aktivasyonKontrol(aktivasyonKodu)
        while True:
            if durum==True:
                self.veriKaydet(kullaniciAdi,sifre,mail)
                break
            else:
                print("Aktivasyon kodunuz hatalı...")
                time.sleep(2)
                self.menuDon()
    def kayitVarmi(self,kulaniciAdi,mail):
        self.veriler=self.veriAl()
        try:
            for kullanici in self.veriler["Kullanıcılar"]:
                if kullanici["Kullanıcıadı"]==kulaniciAdi and kullanici["Mail"]==mail:
                    return True
        except KeyError:
            return False
        return False

    def aktivasyonGonder(self):
        with open("{YourPath}/Aktivasyon.txt","w", encoding="utf-8") as Dosya:
            aktivasyon=str(random.randint(10000,99999))
            Dosya.write("Aktivasyon kodunuz:" + aktivasyon)
        return aktivasyon

    def aktivasyonKontrol(self,aktivasyon):
        aktivasyonKoduAl=input("Lüften mailinize gelen aktivasyon kodunu giriniz:")
        if aktivasyon==aktivasyonKoduAl:
            return True
        else:
            return False

    def veriAl(self):
        try:
            with open("{YourPath}/Kullanıcılar.json","r", encoding="utf-8") as Dosya:
                veriler=json.load(Dosya)
        except FileNotFoundError:
            with open("{YourPath}/Kullanıcılar.json","w", encoding="utf-8") as Dosya:
                Dosya.write("{}")
            with open("{YourPath}/Kullanıcılar.json","r", encoding="utf-8") as Dosya:
                veriler=json.load(Dosya)
        return veriler
            
    def veriKaydet(self,kullaniciAdi,sifre,mail):
        self.veriler=self.veriAl()

        try:
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":kullaniciAdi,"Sifre":sifre,"Mail":mail})
        except KeyError:
            self.veriler["Kullanıcılar"]=list()
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":kullaniciAdi,"Sifre":sifre,"Mail":mail})

        with open("{YourPath}/Kullanıcılar.json","w", encoding="utf-8") as Dosya: 
            json.dump(self.veriler,Dosya,ensure_ascii=False,indent=4)
            print("Kayıt başarılı şekilde oluşturulmuştur...")
        self.menuDon()

    def cikis(self):
        print("Siteden çıkılıyor...")
        time.sleep(2)
        self.dongu=False
        exit()

    def menuDon(self):
        while True:
            x=input("Ana menüye dönmek için 5 e, çıkmak için lüftenn 4 e basınız...: ")
            if x=="5":
                print("Ana menüye dönülüyor...")
                time.sleep(2)
                self.program()
                break
            elif x=="4":
                self.cikis()
                break
            else:
                print("Lüften geçerli bir seçim yapınız..")









Sistem=Site()
while Sistem.dongu:
    Sistem.program()
