import pandas as pd
seri1=pd.DataFrame({
    "Sehir":["Ankara","İstanbul","İzmir","Eskişehir"],
    "Sıcaklık":[30,45,28,30]
})

seri2=pd.DataFrame({
    "Sehir":["Ankara","İstanbul","İzmir","Mersin"],
    "Havadurumu":["Yağmurlu","Bulutlu","Açık","Kapalı"]
})

# sonuc=pd.merge(seri1,seri2,on="Sehir",how='left')
# #  Sehir  Sıcaklık Havadurumu
# # 0     Ankara        30   Yağmurlu
# # 1   İstanbul        45    Bulutlu
# # 2      İzmir        28       Açık
# # 3  Eskişehir        30        NaN

# sonuc=pd.merge(seri1,seri2,on="Sehir",how='right')
# #  Sehir  Sıcaklık Havadurumu
# 0    Ankara      30.0   Yağmurlu
# 1  İstanbul      45.0    Bulutlu
# 2     İzmir      28.0       Açık
# 3    Mersin       NaN     Kapalı

# sonuc=pd.merge(seri1,seri2,on="Sehir",how='outer')
# # Sehir  Sıcaklık Havadurumu
# # 0     Ankara      30.0   Yağmurlu
# # 1  Eskişehir      30.0        NaN
# # 2     Mersin       NaN     Kapalı
# # 3   İstanbul      45.0    Bulutlu
# # 4      İzmir      28.0       Açık

sonuc=pd.merge(seri1,seri2,on="Sehir",how='inner')
# # Sehir  Sıcaklık Havadurumu
# # 0    Ankara        30   Yağmurlu
# # 1  İstanbul        45    Bulutlu
# # 2     İzmir        28       Açık


print(sonuc)