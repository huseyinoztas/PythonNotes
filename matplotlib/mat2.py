import matplotlib.pyplot as plt
import numpy as np

plt.title("Ornek Grafik")
plt.xlabel("Yıl")
plt.ylabel("Adet")
Yil=["2015","2016","2017","2018","2019","2020","2021"]
seri1=[10,8,5,15,25,35,12]
seri2=np.sqrt(seri1)
plt.plot(Yil,seri1,label="Seri1",color="red",marker="o",ms=10,mec="blue",mfc="green")
plt.plot(Yil,seri2,label="Seri2")
plt.legend()##labelların görünmesi için
plt.grid()##arka plandaki grid yapısını düzenler
plt.show()








# plt.figure()
# plt.axis()
# plt.title("Örnek çizgi grafik")
# plt.xlabel("Yıllar")
# plt.ylabel("Fiyatlar")
# x=["2016","2017","2018","2019","2020","2021"]
# y=[100,200,300,150,250,350]
# z=y-np.mean(y)
# plt.plot(x, y)
# plt.plot(x,z)
# plt.show()