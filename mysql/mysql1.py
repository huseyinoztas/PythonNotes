import mysql.connector
veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    password="{Password}",
    database="ornek"
)

yeni=veritabani.cursor()
yeni.execute("SELECT * FROM ornek.ornek")
for i in yeni:
    print(i)