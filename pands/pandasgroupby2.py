import pandas as pd
veri=pd.DataFrame(pd.read_excel("{YourData}"))
yasort=veri.groupby(["Cinsiyet","İl"])["Yas"].mean()
print(yasort)



## birden fazla gruplama yapıp o illerdeki erkek kadın yas ortalamasını çıkartıyor
# yasort=veri.groupby(["Cinsiyet","İl"])["Yas"].mean() 
# # Erkek     Adana             48.391304
# #           Adıyaman          42.300000
# #           Afyonkarahisar    40.880000
# #           Aksaray           45.655172
# #           Amasya            44.423077
# #                               ...    
# # Kadın     Çorum             44.529412
# #           İstanbul          43.941176
# #           İzmir             46.105263
# #           Şanlıurfa         44.250000
# #           Şırnak            47.189189


# yasort=veri.groupby("Cinsiyet")["Yas"].mean()
# ##gruplama üzerinden ortalama istendiği için erkek kadın yas ortalaması dönüyor
# # Cinsiyet
# # Erkek    45.282931
# # Kadın    45.575218


######
# yasort=veri["Yas"].mean()## gruoplama yapmadan ortalama hesabı
######
# ## Erkek ve kadın hastaların sayılarını bulup oranlamak##
# erkek=veri.groupby("Cinsiyet").get_group("Erkek")["Cinsiyet"].count()
# kadin=veri.groupby("Cinsiyet").get_group("Kadın")["Cinsiyet"].count()
# print(f"Erkek Hasta Oranı % {(erkek/(erkek+kadin))*100} ----- Kadın hasta oranı % {(kadin/(erkek+kadin))*100}")
# ## Erkek Hasta Oranı % 47.22 ----- Kadın hasta oranı % 52.78 ##




