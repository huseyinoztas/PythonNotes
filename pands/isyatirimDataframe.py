import pandas as pd
from numpy import sqrt,log
veri=pd.DataFrame(pd.read_excel("{YourData}"))
print(veri)


veri2=veri.drop("Hacim (TL)",axis=1) ## şeklinde yeni bir değere atarsak istediğimiz veriyi siler

# veri.insert(2,column="Log Fiyat",value=(log(veri["Son Fiyat (TL)"])))##stünu istediğimiz aralığa gönderme ve değer ekleme
# veri["Karekök Fiyat"]=sqrt(veri["Hacim (TL)"])##kendimiz bir stün ekleyip değerini veriyoruz
# print(veri.loc[0:5,"Değişim (%)"])##kesiştiği yerdeki veriyi getirir ve 0 ile 5 indeskleri arasındaki veri döner
# print(veri.loc[5,"Hacim (TL)"])##kesiştiği yerdeki veriyi getirir
# print(veri.loc[0])##isteğimiz indeksteki veriyi almak
# print(veri[["Hisse","Son Fiyat (TL)"]])##istediğimiz değerleri getirir
