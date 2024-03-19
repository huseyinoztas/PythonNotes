import pandas as pd
veri=pd.DataFrame(pd.read_excel("{YourData}"))
veri2=veri.fillna(value="Değer yok")
print(veri2)




# print(veri.notnull())## ile değer olmayan indexleri bulabiliyoruz


# print(veri.isnull().sum()) # hangi satırd kaç boş olduğunu döner
# Ad_Soyad    0
# Cinsiyet    1
# Yas         0
# Mail        1
# İl          3
# Bolum       5


# ## default olarak nan olan satırları bulur ve siler
# veri2=veri.dropna(axis=0)
# print(veri2)

## Bölüm üzerinde nan olan satırları siler
# veri2=veri.dropna(subset=["Bolum"])
# print(veri2)


## boş olan değerleri bulur ve verdiğimiz değeri yazar
# veri2=veri.fillna(value="Değer yok")



