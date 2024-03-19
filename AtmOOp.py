class Musteri:
    def __init__(self,ad,soyad,kartsifre,hesapbakiye,kredikartborc,sonodeme):
        self.ad=ad
        self.soyad=soyad
        self.kartsifre=kartsifre
        self.hesapbakiye=hesapbakiye
        self.kredikartborc=kredikartborc
        self.sonodeme=sonodeme

AhmetHesap=Musteri("Ahmet","Candan","1357",5000,4200,"20/11/2021")
MehmetHesap=Musteri("Mehmet","Duyar","2468",6000,3000,"28/11/2021")
TakılanKart=AhmetHesap

class ATM:
    def __init__(self,atmAd):
        self.atmAd=atmAd
        self.giriskontrol()
        self.dongu=True

    def giriskontrol(self):
        Hak=2
        for i in range(0,3):
            Sifre=input("Lütfen 4 haneli şifrenizi giriniz:")
            if Sifre == TakılanKart.kartsifre:
                self.program()
            elif Sifre!=TakılanKart.kartsifre and Hak!=0:
                print("Hatalı şifre girdiniz. Kalan hakkınız {} ".format(Hak))
                Hak-=1
            elif Sifre!=TakılanKart.kartsifre and Hak==0:
                print("""Şifrenizi 3 defa hatalı girdiğinizden dolayı kartınız bloke olmuştur.
                  Lütfen en yakın şubemize başvurunuz!!!""")
                exit()

    def program(self):
        secim=self.menu()
        if secim==1:
            self.bakiye()
        if secim==2:
            self.kkborc()
        if secim==3:
            self.paracek()
        if secim==4:
            self.parayatir()
        if secim==5:
            self.cikis()

    def menu(self):
        secim=int(input("Merhabalar, {}'a Hoşgeldiniz Sayın {} {}. \n\nLüften yapmak istediğiniz işlemi seçiniz...\n\n[1] Bakiye Sorgulama\n[2] Kredi Kartı Borç sorgulama\n[3] Para çekme\n[4] Para yatırma\n[5] Kart iade\n\nSeçim: ".format(self.atmAd,TakılanKart.ad,TakılanKart.soyad)))
        while secim <1 or secim >5:
            print("\n\nLütfen 1 ve 5 arasında geçerli bir değer giriniz... \nAna menüye dönülüyor... ")
            self.program()
        return secim

    def bakiye(self):
        print("Hesap bakiyeniz: {} TL'dir".format(TakılanKart.hesapbakiye))
        self.dongu=False
        self.menudon()

    def kkborc(self):
        print("Kredi kartı borcunuz {} son ödeme tarihli {} TL'dir".format(TakılanKart.sonodeme,TakılanKart.kredikartborc))
        self.dongu=False
        self.menudon()

    def paracek(self):
        miktar=int(input("Lüften çekeceğiniz tutarı giriniz:..."))
        yeniMiktar=TakılanKart.hesapbakiye-miktar
        if miktar>TakılanKart.hesapbakiye:
            print("Yetersiz bakiye Çekebileceğiniz miktar {} TL'dir".format(TakılanKart.hesapbakiye))
            self.menudon()
        else:
            print("Lüften paranızı sayarak alınız. Hesabınızda kalan tutar {} TL'dir".format(yeniMiktar))
            self.menudon()

    def parayatir(self):
        miktar2=int(input("Lüften yatırılacak tutarı giriniz:..."))
        yeniMiktar2=TakılanKart.hesapbakiye+miktar2
        print("Para yatırma işlemi başarıyla gerçekleşmiştir. Hesabınızın yeni bakiyesi {} TL'dir".format(yeniMiktar2))
        self.menudon()

    def cikis(self):
        print("Bankamızı tercih ettiğiniz için teşekkür eder iyi günler dileriz...")
        self.dongu=False
        exit()

    def menudon(self):
        x=int(input("Ana menüye dönmek için lütfen 7 tuşuna basınız. Kart iade için 5 e basınız...."))
        if x==7:
            self.program()
        elif x==5:
            self.cikis()

Banka=ATM("Xbank")
while Banka.dongu:
    Banka.program()










