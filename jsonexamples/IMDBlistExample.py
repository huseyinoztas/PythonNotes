import json
import time
import re
import textwrap
import requests

class Film:
    def __init__(self):
        self.dongu=True
    def program(self):
        secim=self.menu()

        if secim=="1":
            self.eniyi250()
        if secim=="2":
            self.enpopuler()
        if secim=="3":
            self.sinemalarda()
        if secim=="4":
            self.yakinda()
        if secim=="5":
            self.filmara()
        if secim=="6":
            self.cikis()
        
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-6]",secim):
                raise Exception("Lütfen 1 ve 6 arasında geçerli bir seçim yapınız.")
            while True:
                try:
                    secim=input("Merhabalar, hoş geldiniz\n\nLüften yapmak istediğiniz işlemi seçiniz..\n\n[1] - En iyi 250 film\n[2] - En popüler filmler\n[3] - Sinemalarda\n[4] - Yakında\n[5] - Film Ara\n[6] - Çıkış\n\n ")
                    kontrol(secim)
                except Exception as hata:
                    print(hata)
                    time.sleep(2)
                else:
                    break
            return secim

    def eniyi250(self):
        print("En iyi 250 film listesine ulaşılıyor...\n\n")
        time.sleep(2)
        url=requests.get("imdb.com")##imdb api key alımını değiştirdiği için doğru değerler girilemedi
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()

    def enpopuler(self):
        print("En popüler film listesine ulaşılıyor...\n\n")
        time.sleep(2)
        url=requests.get("imdb.com")##imdb api key alımını değiştirdiği için doğru değerler girilemedi
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()

    def sinemalarda(self):
        print("Sinemalardaki film listesine ulaşılıyor...\n\n")
        time.sleep(2)
        url=requests.get("imdb.com")##imdb api key alımını değiştirdiği için doğru değerler girilemedi
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()

    def yakinda(self):
        print("Yakında çıkacak filmler listesine ulaşılıyor...\n\n")
        time.sleep(2)
        url=requests.get("imdb.com")##imdb api key alımını değiştirdiği için doğru değerler girilemedi
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()
    
    def filmara(self):
        print("Film arama menüsüne ulaşılıyor...")
        time.sleep(2)
        film=input("Lütfen film adını giriniz: ")

        url=requests.get("https://imdb.com")##imdb api key alımını değiştirdiği için doğru değerler girilemedi
        sonuc=url.json()

        ID=list()
        for i in sonuc["items"]:
            ID.append(i["id"])
        
        AD=list()
        for i in sonuc["items"]:
            AD.append(i["title"])
        
        cevir=zip(AD,ID)
        veri=dict(cevir)
        key=veri.get(film)
        
        url2=requests.get("https://imdb.com/{}".format(key))##imdb api key alımını değiştirdiği için doğru değerler girilemedi

        sonuc2=url2.json()
        print(sonuc2["plotShort"]["plainText"])
        self.menudon()

    def cikis(self):
        print("Çıkılıyor...")
        time.sleep(2)
        self.dongu=False
        exit()

    def menudon(self):
        while True:
            x=input("Ana menüye dönmek için 7'ye basınız. Çıkmak için lütfen altıya basınız")
            if x=="7":
                print("Ana menüye dönülüyor..")
                time.sleep(2)
                self.program()
                break
            elif x=="6":
                self.cikis()
                break
            else:
                print("Lütfen geçerli bir seçim yapınız")



Sistem=Film()
while Sistem.dongu:
    Sistem.program()