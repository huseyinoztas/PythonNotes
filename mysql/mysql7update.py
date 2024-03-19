import mysql.connector
baglan=mysql.connector.connect(
    host="localhost",
    user="root",
    password="{Password}",
    database="Ornek"
)
db=baglan.cursor()
###birden fazla satır ve stuna update
# db.execute("update bilgiler set yer='Türkiye2',soyad='XXXX' where id IN (1,2,3,4,5)")
db.execute("delete from bilgiler where id IN (1,2,3,4,5)")## idli veriyi siler
baglan.commit()