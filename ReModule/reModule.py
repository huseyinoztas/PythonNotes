## re modul ile şifre oluşturma1

import re

dogumtarihi="1998"
karakter=[r"\?", r"\*", r"\!", r"\%"]

def sifrekontrol(sifre):
    if len(sifre)<8:
        raise Exception("Sifreniz en az 8 karakterden oluşmalıdır.")
    elif not re.search("[a-z]", sifre):
        raise Exception("Sifreniz en az 1 tane küçük harf içermelidir.")
    elif not re.search("[A-Z]", sifre):
        raise Exception("Sifreniz en az 1 tane büyük harf içermelidir.")
    elif not re.search("[0-9]",sifre):
        raise Exception("Sifreniz en az 1 tane rakam içermelidir.")
    elif not re.search(str(karakter), sifre):
        raise Exception("Sifreniz en az 1 tane karakter içermelidir.")
    elif sifre.startswith(dogumtarihi)==True:
        raise Exception("Sifreniz doğum tarihi ile başlayamaz.")
    elif sifre.endswith(dogumtarihi)==True:
        raise Exception("Sifreniz doğum tarihi ile bitemez.")
    else:
        print("Şifreniz başarılı bir şekilde oluşturulmuştur.") 
    
while True:
    try:
        sifre=input("Lüften şifrenizi oluşturunuz...:")
        sifrekontrol(sifre)
    except Exception as hata:
        print(hata)
    else:
        break



