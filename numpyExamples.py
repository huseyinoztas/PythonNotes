import numpy as np
    


x=np.array([1,2,3,6,7,8,12])
y=np.array([1,3,9,7,54,4])
print(np.union1d(x,y))


## unique() fonksiyonu tekrarlanan değerli kaldırır
## sort() sıralar...
# x=np.array([1,2,3,6,7,8,12])
# y=np.array([1,3,9,7,54,4])
# print(np.union1d(x,y)) #[ 1  2  3  4  6  7  8  9 12 54]
# #birleşimini veriyor bu fonksiyon da
##
# x=np.array([1,2,3,6,7,8,12])
# y=np.array([1,3,9,7,54,4])
# print(np.setdiff1d(x,y)) #[ 2  6  8 12]
# xte olup y de olmayan elemanları verir
# ##
##
# x=np.arange(11)
# y=np.delete(x,[0,4]) #sıfırınca ve dörtüncü indeksi siler
##
# bir=np.random.randint(0,10,size=(3,4)) 3 e 4 lük 0-10 arasında matris
# bir=np.random.rand(3,4) 3 e 4 lük bir random çıktı
# bir=np.linspace(0,100,5, endpoint=False) # [ 0. 20. 40. 60. 80.] 0 dan 100 rakamları arasında 5 elemanlı bir liste oluştururu
# bir=np.linspace(0,100,5) # [  0.  25.  50.  75. 100.] 0 dan 100 rakamları arasında 5 elemanlı bir liste oluşturup aralığı otomatik kendisi veriri
# bir=np.arange(0,100,5) #0 dan 100 e kadar olan sayıları 5 5 arttırarak liste oluşturur
# diyagonal=np.diag([1,2,3,4,5]) #köşegenleri 1,2,3,4,5 ten oluşan matris yapısı
# diyagonal=np.eye(5) köşeleri birlerden oluşan
# onlar=np.ones((3,4),dtype=int)*10 #10 lardan oluşan bir matris
# yirmiler=np.full((5,5),20,dtype=int) #20 lerden oluşan bir matris
# sıfır=np.zeros((5,5),dtype=int) #sıfırlardan oluşan bir matris
# bir=np.ones((3,4),dtype=int) #birlerden oluşan bir matris

#İLK DERS
# dizi=np.array([1,2,3,4,5,6,7,8])
# print(type(dizi))
# dizi2=np.array([[1,2],[3,4],[5,6],[7,8]]) ##Bu şekilde olunca matris yapısıyla dönüyor
# print(dizi2.shape) ## çıktısı (4,2) 4 satır 2 sütun
# dizi3=dizi.reshape(4,2) #ile otomatik yapıyoruz 
# print(dizi3)
