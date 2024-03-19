
### SINIF YARATMA ####
# class Insan:  #bu şekilde de sınıf yaratılıyor
#     Ad="Mehmet"
#     soyad="Can"
#     Yas=22
#     Sacrengi="Siyah"

# class Insan2:   #bu şekilde de yaratılıyor
#     def __init__(self,Ad,Soyad,Yas,Sacrengi):
#         self.Ad=Ad
#         self.Soyad=Soyad
#         self.Yas=Yas
#         self.Sacrengi=Sacrengi

# Insan1=Insan2("mehmet","candan",63,"beyaz")
# Insan3=Insan2("nimet","candan",62,"beyaz")

### METOT YARATMA ####
# class Insan:   
#     def __init__(self,Ad,Soyad,Dogumyılı):
#         self.Ad=Ad
#         self.Soyad=Soyad
#         self.Dogumyılı=Dogumyılı
#     def bilgi(self):
#         print("merhaba benim adım {}, soyadım {}, {} yılında doğdum".format(self.Ad,self.Soyad,self.Dogumyılı))
#     def yas(self):
#         return 2021-self.Dogumyılı
        
# Insan1=Insan("ahmet","can",1998)
# Insan2=Insan("mehmet","candan",1993)

# Insan1.bilgi()
# Insan2.bilgi()

# print(Insan1.yas())
# print(Insan2.yas())


#### KAPSÜLLEME ##### ERİŞİME ENGELLEME
### __ ile kapsülleme yapıyoruz
# class Memur:
#     def __init__(self,Ad,Soyad,Maas):
#         self.Ad=Ad
#         self.Soyad=Soyad
#         self.__Maas=Maas
#         self.__zam=0.20
#     def zamoran(self):
#         self.__Maas=self.__Maas+self.__Maas*self.__zam

#     def getMaas(self):  ##kapsüllenen değeri görmek için get ile alıyoruz
#         return self.__Maas
#     def getZam(self):
#         return self.__zam
#     def setZam(self,yeniOran):
#         self.__zam=yeniOran


# memur1=Memur("ahmet","can",6000)

# memur1.setZam(0.5)
# memur1.zamoran()
# print(memur1.getMaas())


### KALITIM-MİRAS-İNHERİTANCE ###

# class Insan():
#     def __init__(self,Ad,Soyad,Sacrengi,Boy,Kilo):
#         self.Ad=Ad
#         self.Soyad=Soyad
#         self.Sacrengi=Sacrengi
#         self.Boy=Boy
#         self.Kilo=Kilo

# class Ogrenci(Insan):
#     def __init__(self, Ad, Soyad, Sacrengi, Boy, Kilo,Bolum,Yas):
#         super().__init__(Ad, Soyad, Sacrengi, Boy, Kilo)
#         self.Yas=Yas
#         self.Bolum=Bolum


# Insan1=Insan("mustafa","can","siyah",183,82)
# Ogrenci1=Ogrenci("ali","can","kumral",175,80,"fen",19)

# print(Insan1.Kilo)
# print(Ogrenci1.Bolum)







