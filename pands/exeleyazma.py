import pandas as pd

seri1=pd.DataFrame({
    "Ad":["Ali","Veli","Can"],
    "Soyad":["Aslan","Narlı","Bozgun"]
})

seri2=pd.DataFrame({
    "Sehir":["Ankara","İstanbul","İzmir"],
    "Sıcaklık":[15,19,25]
})

##çok sayfalı excele yazdırma
with pd.ExcelWriter("{YourData}") as writer:
    seri1.to_excel(writer,sheet_name="Ad_soyad",index=False)
    seri2.to_excel(writer,sheet_name="Hava",index=False)


##Tek sayfalı standar excel yazma komutu
# dosya=seri1.to_excel("{YourData}",sheet_name="Ad_soyad",index=False)
