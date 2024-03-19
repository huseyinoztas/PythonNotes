### Aggregate Functions ###

import mysql.connector
baglan=mysql.connector.connect(
    host="localhost",
    user="root",
    password="{Password}",
    database="Ornek"
    )
db=baglan.cursor()
# db.execute("Select count(*) from ornek.bilgiler where yer='Ankara'")###Kaç tane veri olduğunu sayıyor
# db.execute("Select avg(yas) from ornek.bilgiler")##Total yaş ortalaması
# db.execute("Select max(yas) from ornek.bilgiler")##max min ile listeleri çekebiliyoruz
# db.execute("Select*from ornek.bilgiler where yas=(Select max(yas) from ornek.bilgiler)")##yaşı max olan herkesi liste halinde getirir
sorgu=db.fetchall()

for i in sorgu:
    print(i)
