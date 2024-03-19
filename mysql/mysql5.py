import mysql.connector
baglan=mysql.connector.connect(
    host="localhost",
    user="root",
    password="{Password}",
    database="Ornek"
    )
db=baglan.cursor()
# db.execute("Select*from Ornek.bilgiler order by ad")##isme göre sıralama
db.execute("Select*from Ornek.bilgiler order by yas")##küçükten büyüğe yaş sıralaması
db.execute("Select*from Ornek.bilgiler order by yas desc")##büyükten küçüğe yaş sıralaması

sorgu=db.fetchall()


for i in sorgu:
    print(i)

