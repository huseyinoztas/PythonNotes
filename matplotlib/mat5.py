import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,9,20)
y=x**2
z=x**3
fig,grafik=plt.subplots(nrows=2,ncols=1)
grafik[0].plot(x,y)
grafik[0].set_title("1. Grafik")
grafik[1].plot(x,z)
grafik[1].set_title("2. Grafik")
plt.tight_layout()
fig.savefig("{YourPath}")


# fig=plt.figure()
# grafik1=fig.add_axes([0.1,0.1,0.8,0.8])
# grafik1.plot(x,y,c="Red")
# grafik1.set_xlabel("X değerleri")
# grafik1.set_ylabel("Y değerleri")
# grafik1.set_title("Örnek Grafik")

# grafik2=fig.add_axes([0.3,0.6,0.2,0.2])
# grafik2.plot(x,z,c="Blue")
# grafik2.set_xlabel("X değerleri")
# grafik2.set_ylabel("z değerleri")
# grafik2.set_title("Örnek Grafik")

# ##grafik içinde grafik gösterimi

# plt.show()



# fig=plt.figure()
# konum=fig.add_axes([0.1,0.1,0.8,0.6])
# yil=["2018","2019","2020","2021"]
# fiyat=[1500,2500,3500,4800]
# konum.plot(yil,fiyat)
# konum.set_xlabel("Yil")## obje üzerinden yapıldığı için set kullanılmalı 
# konum.set_ylabel("Fiyat")
# konum.set_title("Fiyat Grafiği")
# plt.show()