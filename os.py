import os
import random

# 20 ile 45 arasında rastgele sayılar oluştur
rastgele_sayilar = [random.randint(20, 45) for _ in range(5000)]

print(rastgele_sayilar)


# os.mkdir("Merhaba")

## import os ile os.mkdir ile bulunduğun dizinde klasör oluşturabiliyorsunuz
## os.makedirs("Merhaba/merha") ile klasör ve alt klasör oluşturulabiliyor. 
## os.removedirs("Merhaba") klasörü silme

# ## o klasördeki dosyaları görüntüleme
# y=('C:\\Users\husey\OneDrive\Masaüstü\python') ## C: den sonra bir ters slaş daha ekle
# x=os.listdir(y)
# print(x)

# os.system("notepad.exe") sistemde tanımlı uygulamaları açar

