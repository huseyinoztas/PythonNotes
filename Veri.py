# import random
# random_side=random.randint(0,1)
# if random_side == 1:
#   print("heads")
# else:
#   print("Tails")

# names_string=input()
# names=names_string.split(",")
# import random
# num_items = len(names)
# random_choice = random.randint(0,num_items-1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + "is going to buy meal today")

# import random
# import string

# sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# harfler = string.ascii_letters  # ascii_letters, tüm harfleri içeren bir string

# # Rastgele 4 sayı, 2 büyük harf ve 2 küçük harf seçme
# sayi_secilenler = [str(random.choice(sayilar)) for _ in range(4)]
# buyuk_harf_secilenler = [random.choice(harfler.upper()) for _ in range(2)]
# kucuk_harf_secilenler = [random.choice(harfler.lower()) for _ in range(2)]

# # Tüm seçilenleri karıştırarak şifreyi oluşturma
# password_list = sayi_secilenler + buyuk_harf_secilenler + kucuk_harf_secilenler
# random.shuffle(password_list)
# password = ''.join(password_list)

# print(password)


# # ortalama hesaplama
# def ortalama(*args):
#     sonuc=0
#     for i in args:
#         sonuc=sonuc+i
#         sonuc2=sonuc/len(args)
#     return round(sonuc2,3)
# print(ortalama(5,10,15))

# def faktoriyel(x):
#     sonuc=1
#     for i in range(1,x+1):
#         sonuc=sonuc*i
#     return int(sonuc)
    
# result=faktoriyel(4)
# print(result)


# toplam=lambda x,y:x+y #tek satırda fonksiyon
# print(toplam(2,7))

# kare=lambda sayi:sayi**2
# liste=[1,3,5,7,9]
# sonuc=list(map(kare,liste)) #map yapısı kullanımı
# print(sonuc)