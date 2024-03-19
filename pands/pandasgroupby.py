import pandas as pd

veri=pd.DataFrame(pd.read_excel("{YourData}"))
bolgeler=veri.groupby("BOLGE").get_group("GAZİEMİR")
bolgeler2=veri.groupby("BOLGE").get_group("NARLIDERE")
print(bolgeler)
print(bolgeler2)



## grupladığımız veriden istediğimiz bölgenin çıktısı
# bolgeler=veri.groupby("BOLGE").get_group("GAZİEMİR")
# print(bolgeler)

## Bu şekilde gruplanmış verilerin çıktısını alabiliriz
# bolgeler=veri.groupby("BOLGE")
# for i in bolgeler:
#     print(i)