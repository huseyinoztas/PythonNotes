dosya=open("Merhaba.txt","w") # yeni bir doya oluşturma, var olan dosyayı siler yenisini oluşturur
# dosya=open("Merhaba.txt","x") # yeni bir dosya oluşturur ama aynı adda dosya varsa hata verir.
# dosya=open("Merhaba.txt","a") # a ile olan dosyanın içine yazar
# dosya.write("merhaba benim adım anlasilir ekonomi.") #dosya içine yazı yazmak için

## içindekileri okumak için yazmamız gereken komutlar
# dosya=open("Merhaba.txt","r")
# print(dosya.read()) 

dosya.close() #close demediğimizde arka planda çalışır

