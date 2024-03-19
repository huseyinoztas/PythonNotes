import matplotlib.pyplot as plt
import numpy as np
calismasaati=[1.75,1.5,0.5,3,3.25,2]
puan=[17,15,7,19,20,16]
plt.title("Not dağılım grafiği")
plt.xlabel("Saat")
plt.ylabel("Puan")
plt.axis([0,4,0,21])
renkler=np.random.randint(0,100,6)
plt.scatter(calismasaati,puan,s=100,c=renkler,cmap="Reds")
plt.colorbar()
plt.show()