from bs4 import  BeautifulSoup

kod="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Deneme amaçlı eğitimde açılan html doc</h1>
</body>
</html>"""

parset=BeautifulSoup(kod,"html.parser")

yaz=parset.body
print(yaz)