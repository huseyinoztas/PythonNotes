import pandas as pd
veri=pd.DataFrame(pd.read_excel("{YourData}"))

seat=veri.groupby("Marka").get_group("Seat")
print(seat.groupby("Arac Tip Grubu")["Fiyat"].mean())



##Araç tipine göre gruplama ve sonrasında o aracın modellerine göre fiyat ortalaması alma
# seat=veri.groupby("Marka").get_group("Seat")
# print(seat.groupby("Arac Tip Grubu")["Fiyat"].mean())


# print(veri.groupby("Marka")["Fiyat"].mean().sort_values()) ## markaya göre gruplayıp ortalamasını alıp sıralıyoruz
# print(veri.sort_values("Fiyat",ascending=False))## Yüksekten düşüğe sıralama
# print(veri.sort_values("Fiyat"))## düşükten yükseğe sıralama
# print(veri[veri["Km"].min()==veri["Km"]])## km 0 olan arabanın hangi satırda olduğunu aramak
# print(veri["Model Yıl"].mean())## model yıllarının ortalaması
# print(veri[100:].head(21))## index 100den başlayıp 121 de bitiriyor.
# print(veri.tail())## sondan 5 satırı default içine ne yazarsak o kadar satır döndürür
# print(veri.head())## ilk 5 satırı default olarak içine ne yazarsak da o kadar satır getirir
# print(len(veri.index))## 9044
# print(len(veri.columns))## 15

# print(veri.columns)
# # Index(['İlan Tarihi', 'Marka', 'Arac Tip Grubu', 'Arac Tip', 'Model Yıl',
# #        'Yakıt Turu', 'Vites', 'CCM', 'Beygir Gucu', 'Renk', 'Kasa Tipi',
# #        'Kimden', 'Durum', 'Km', 'Fiyat'],
# #       dtype='object')



# print(veri.index)
## RangeIndex(start=0, stop=9044, step=1)