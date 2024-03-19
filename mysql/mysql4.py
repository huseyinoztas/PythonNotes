import mysql.connector
baglan=mysql.connector.connect(
    host="localhost",
    user="root",
    password="{Password}",
    database="Ornek"
    )
db=baglan.cursor()
db.execute("Select ad,soyad,tc,yas from Ornek.bilgiler where cinsiyet='Kadın' and yas<35 and yer='İzmir'")
sorgu=db.fetchall()

for i in sorgu:
    print(i)
