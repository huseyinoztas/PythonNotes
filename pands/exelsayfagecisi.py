import pandas as pd
veri=pd.ExcelFile("{YourData}")
# veri=pd.DataFrame(pd.read_excel("{YourData}",sheet_name="Doktor"))

for i in range(0,len(veri.sheet_names)):
    veri2=pd.DataFrame(pd.read_excel(veri,sheet_name=veri.sheet_names[i]))
    print(veri2)



##veri=pd.ExcelFile("{YourData}").sheet_names ile sayfaların isimlerine ulasabiliyoruz
##['Hasta', 'Ulke', 'il', 'İlce', 'Doktor', 'Kan', 'Bolum', 'Kurum']

## sheet_name="Doktor" göndererek isim yada index ile o sayfadaki veriye ulaşabiliyoruz
###veri=pd.DataFrame(pd.read_excel("{YourData}",sheet_name="Doktor"))####


