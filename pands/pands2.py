import pandas as pd
import numpy as np

# Veri=[["Elma",10],["armut",15],["çilek",20]]
# baslik=["ürün","fiyat"]
# satırNo=[1,2,3]
# veriler=pd.DataFrame(Veri,columns=baslik,index=satırNo)

# print(veriler) 
# #     ürün  fiyat
# # 1   Elma     10
# # 2  armut     15
# # 3  çilek     20


# df=pd.DataFrame([["Elma",10],["armut",15],["çilek",20]],columns=["Ürünler","Fiyat"])
# print(df)
# #    Ürünler  Fiyat
# # 0    Elma     10
# # 1   armut     15
# # 2   çilek     20


# seri1=[1,2,3,4,5]
# seri2=[5,7,1,3,8]

# baslikliVeri=dict(ürün1=seri1,ürün2=seri2)
# veriler=pd.DataFrame(baslikliVeri)
# print(veriler)
# #     ürün1  ürün2
# # 0      1      5
# # 1      2      7
# # 2      3      1
# # 3      4      3
# # 4      5      8