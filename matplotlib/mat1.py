import matplotlib.pyplot as plt

yil=[2015,2016,2017,2018,2019,2020,2021]
Fiyat=[100,200,300,400,500,600,700]
plt.plot(yil,Fiyat,color="red",linewidth=3) 
plt.axis([2015,2025,0,1000])
plt.title("2015-2021 Fiyat verileri")
plt.xlabel("Yıl")
plt.ylabel("Fiyat")
plt.show()



# plt.plot(seri1,seri2) ## ilk parametre x i ikinci parametre y yi gösterir



