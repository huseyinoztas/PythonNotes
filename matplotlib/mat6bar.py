import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
grafik=fig.add_axes([0.1,0.1,0.8,0.6])
siniflar=["A","B","C","D","E"]
index=np.arange(len(siniflar))
a=0.25
matematik=[90,55,75,45,35]
turkce=[80,58,77,90,65]
fizik=[40,35,68,78,80]
grafik.bar(index-a,matematik,label="Matematik",color="Red",width=a)
grafik.bar(index,turkce,label="Türkçe",color="Blue",width=a)
grafik.bar(index+a,fizik,label="Fizik",color="Green",width=a)
grafik.set_title("Sınıflara göre ortalama not dağılımı")
grafik.set_xlabel("Sınıflar")
grafik.legend()
grafik.set_xticks(ticks=index,labels=siniflar)##indekslere sınıfların gelmesi için yapıyoruz
plt.show()












# araclar=["Fiat","Ford","BMW","Mercedes"]
# fiyatlar=[100,300,500,900]
# grafik.bar(araclar,fiyatlar,label="Ortalama fiyat")
# grafik.set_title("Fiyat Bar grafiği")
# grafik.set_xlabel("Araçlar")
# grafik.legend()
# plt.show()