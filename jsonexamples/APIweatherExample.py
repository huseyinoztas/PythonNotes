import requests
import json

while True:

    sehir=input("Lüften hava durumunu öğrenmek istediğiniz şehri giriniz.")
    apiKey="{API_KEY}"
    adress="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric".format(sehir,apiKey)

    connect=requests.get(adress)
    sorgu=connect.json()
    
    havaDurumu=sorgu["weather"][0]["description"]
    havaSicaklik=sorgu["main"]["temp"]
    hissedilenSicaklik=sorgu["main"]["feels_like"]
    minSicaklik=sorgu["main"]["temp_min"]
    maxSicaklik=sorgu["main"]["temp_max"]
    basinc=sorgu["main"]["pressure"]
    nem=sorgu["main"]["humidity"]

    print("{} İçin hava durumu bilgileri aşağıdaki gibidir.\n\nSıcaklık: {} °\nDurum: {}\nHissedilen Sıcaklık: {} °\nEn düşük sıcaklık: {} °\nEn yüksek sıcaklık: {} °\nBasınç: {} hpa\nNem: {} %".format(sehir.capitalize(),havaSicaklik,havaDurumu.title(),hissedilenSicaklik,minSicaklik,maxSicaklik,basinc,nem))
