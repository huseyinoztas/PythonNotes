with open("Merhaba.txt","r",encoding="utf-8") as dosya:
    # dosya.seek(9) # istediğimiz karakterden itibaren okumaya başlar.
    print(dosya.read())