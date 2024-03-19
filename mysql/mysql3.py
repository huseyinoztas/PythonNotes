import mysql.connector
baglan=mysql.connector.connect(
    host="localhost",
    user="root",
    password="{Password}",
    database="Ornek"
    )
db=baglan.cursor()
# sorgu=("Create Table Bilgiler(id INT(5) UNSIGNED AUTO_INCREMENT PRIMARY KEY, Ad VARCHAR(25) NOT NULL, Soyad VARCHAR(25) NOT NULL, Tc VARCHAR(11) NOT NULL, Cinsiyet VARCHAR(5) NOT NULL, Yas INT NOT NULL, Yer VARCHAR(20) NOT NULL)")

db.execute("Select id, Ad,Soyad,Yer from Ornek.bilgiler")
sorgu=db.fetchall()

for i in sorgu:
    print(i)

