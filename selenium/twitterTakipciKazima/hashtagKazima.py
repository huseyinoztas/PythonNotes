from xbilgi import kullaniciAdi,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("excludeSwitches",["enable-logging"])
service=Service("{YourDriverPath}")
driver = webdriver.Chrome(service=service,options=options)
url="https://twitter.com/i/flow/login"

driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)

##GİRİŞ##
ka=driver.find_element(By.XPATH,"//input[@autocomplete='username']")  #kullanıc
ka.send_keys(kullaniciAdi)
time.sleep(2)
ka.send_keys(Keys.ENTER)
time.sleep(2)
sif=driver.find_element(By.XPATH,"//input[@autocomplete='current-password']")
sif.send_keys(sifre)
time.sleep(2)
sif.send_keys(Keys.ENTER)
time.sleep(2)

aranan="faiz"
arama="https://twitter.com/search?q={}&src=typed_query&f=live".format(aranan)
driver.get(arama)
time.sleep(5)

bilgi=[]
profil=driver.find_elements(By.CSS_SELECTOR,".css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu")
for i in profil:
    bilgi.append(i.text)

tweetsayisi=50

while True:
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(2)
    profil2=driver.find_elements(By.CSS_SELECTOR,".css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu")
    for j in profil2:
        x=j.text
        if x not in bilgi:
            bilgi.append(x)
    if len(bilgi)>=tweetsayisi:
        break

sayac=1
for k in range(0,tweetsayisi):
    kisi=(bilgi[k].split("\n")[1])
    tweet=(bilgi[k].split("\n")[4])
    print(f"{sayac}-{kisi}: {tweet}")
    sayac+=1
    sayac=sayac

time.sleep(5)