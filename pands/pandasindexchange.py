import pandas as pd
veri=pd.DataFrame(pd.read_excel("{YourData}"))
veri.set_index("Tc",inplace=True)
sorgu=int(input("Lütfen tc giriniz"))
print(veri.loc[sorgu])



# ## bu şekilde tcsi girilen kişinin bilgisi gelir indexlemeyi tc üzerinden yaptığımız için
# veri.set_index("Tc",inplace=True)
# sorgu=int(input("Lütfen tc giriniz"))
# print(veri.loc[sorgu])



# ##ana veri üzerinde index değişimi yapmak
# veri.set_index("Tc",inplace=True)
# veri.reset_index() ## ile index resetlenir eski haline gelir