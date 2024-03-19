import pandas as pd

veri=pd.DataFrame(pd.read_excel("{YourData}"))
filtre=veri[(veri["Değişim (%)"]>4)&(veri["Son Fiyat (TL)"]>202)]
print(filtre)


# filtre=veri[(veri["Değişim (%)"]>4)&(veri["Son Fiyat (TL)"]>202)] ## Koşullu filtreleme & eklenerek + şart ekleniyor | yada da eklenebilir.
# print(veri[veri["Değişim (%)"]>7])# %7 den fazla değişimi olan hisseleri filtreleme
# print(veri[5:][["Hisse","Son Fiyat (TL)"]].head(15))#5 ten başlayıp 15 değer getiriyor
# print(veri[["Hisse","Son Fiyat (TL)"]].head(15))##birden fazla stün için liste olarak gönderilmeli
# print(veri["Son Fiyat (TL)"].head(15))#istediğimiz stündaki ilk 15 veri
# print(veri.tail(15))#son 15 veriyi getirir
# print(veri.tail())#son 5 veriyi getirir
# print(veri.head())#ilk 5 veriyi getirir
# print(veri.head(15))#ilk 15 veriyi getirir