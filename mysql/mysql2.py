import mysql.connector
baglan=mysql.connector.connect(
    host="localhost",
    user="root",
    password="{Password}",
    database="Hastane"
    )

db=baglan.cursor()
# sorgu=("Create Table Bilgiler(id INT(5) UNSIGNED AUTO_INCREMENT PRIMARY KEY, Ad VARCHAR(15) NOT NULL, Soyad VARCHAR(15) NOT NULL, DogumYeri VARCHAR(15) NOT NULL)")
sorgu=("INSERT INTO hastane.bilgiler(Ad,Soyad,Dogumyeri) VALUES('Mehmet','Aslan','İstanbul')")
db.execute(sorgu)
baglan.commit()