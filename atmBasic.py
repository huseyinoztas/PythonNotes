print("""\t*****Merhabalar XBank'a Hoşgeldiniz.*****
      \t\tLütfen Kartınızı Takınız...""")

Veritabanı = {
"AhmetHesap":{
    "İsim":"Ahmet",
    "Soyisim":"Candan",
    "KartSifre":"1357",
    "HesapBakiye":5000,
    "KrediKartBorc":4200,
    "KrediKartBorcTarih":"20/11/2021"
    },
"MethmetHesap":{
    "İsim":"Mehmet",
    "Soyisim":"Duyar",
    "KartSifre":"2468",
    "HesapBakiye":6000,
    "KrediKartBorc":3800,
    "KrediKartBorcTarih":"20/11/2021"
    }
}

TakılanKart=dict(Veritabanı["AhmetHesap"])
Hak=2
for i in range(0,3):
    Sifre=input("Lütfen 4 haneli şifrenizi giriniz")
    if Sifre ==TakılanKart.get("KartSifre"):
        print("""Merhaba, Hoşgeldiniz Sayın{}{}
        Lütfen yapmak istediğiniz işlemi seçiniz...""".
        format(TakılanKart.get("İsim"),TakılanKart.get("Soyisim")))
        Sec=input("""
        [1] Bakiye sorgulama
        [2] Kredi kartı borcu sorgulama
        [3] Para çekme
        [4] Para yatırma
        [Q] Kart İade\n""")
        break
    elif Sifre !=TakılanKart.get("KartSifre") and Hak!=0:
        print("Hatalı şifre girdiniz. Kalan Hakkınız{}".format(Hak))
        Hak-=1
    elif Sifre!=TakılanKart.get("KartSifre") and Hak==0:
        print("""Şifrenizi 3 defa hatalı girdiğiniz için kartınız bloke olmuştur
              lüften en yakın şubemize başvurunuz""")
        exit()
if Sec=="1":
    print("""Hesap bakiyeniz {} TL'dir.""".format(TakılanKart.get("HesapBakiye")))
elif Sec=="2":
    print("""Kredi kartı borcunuz: {} Son ödeme tarihli {} TL'dir""".
          format(TakılanKart.get("KrediKartBorcTarih"),TakılanKart.get("KrediKartBorc")))
elif Sec=="3":
    Miktar1=int(input("Lüften çekilecek miktarı yazınız"))
    if TakılanKart.get("HesapBakiye")<Miktar1:
        print("Yetersiz bakiye")
    else:
        print("Lütfen paranızı kontrol ederek alınız")
        YeniBakiye1=TakılanKart.get("HesapBakiye")-Miktar1
        print("Geriya kalan bakiyeniz {} TL'dir".format(YeniBakiye1))
elif Sec=="4":
    Miktar2=int(input("Lüften yatırılacak miktarı giriniz : "))
    print("Paranız hesabınıza yatırılmıştır. Teşekkür ederiz") 
    YeniBakiye2=TakılanKart.get("HesapBakiye")+Miktar2  
    print("Geriya kalan bakiyeniz {} TL'dir".format(YeniBakiye2)) 
elif Sec=="Q" or Sec=="q":
    print("Teşekkür eder, iyi günler dileriz")
    exit()
else:
    print("Lütfen geçerli bir giriş yapınız")  