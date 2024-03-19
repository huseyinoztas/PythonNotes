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

##TAKİPÇİ SAYFASI##
url="https://twitter.com/{user}"
driver.get(url)
time.sleep(7)
onaylitakipci=driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-14lw9ot.r-jxzhtn.r-13l2t4g.r-1ljd8xs.r-1phboty.r-16y2uox.r-184en5c.r-61z16t.r-11wrixw.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div > div:nth-child(3) > div > div > div > div > div.css-175oi2r.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a")
onaylitakipci.click()
time.sleep(2)
takipci=driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-14lw9ot.r-jxzhtn.r-13l2t4g.r-1ljd8xs.r-1phboty.r-16y2uox.r-184en5c.r-61z16t.r-11wrixw.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div > div.css-175oi2r.r-aqfbo4.r-gtdqiz.r-1gn8etr.r-1g40b8q > div.css-175oi2r.r-1e5uvyk.r-6026j > div:nth-child(2) > nav > div > div.css-175oi2r.r-1adg3ll.r-16y2uox.r-1wbh5a2.r-1pi2tsx > div > div:nth-child(3) > a")
takipci.click()
time.sleep(5)

divliste=[]

liste1=driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div").find_elements(By.CSS_SELECTOR,".css-1rynq56.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-18u37iz.r-1wvb978")
time.sleep(3)                                 

for j in liste1:
    divliste.append(j.text)

sonyukseklik=driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(5)
    liste2=driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div").find_elements(By.CSS_SELECTOR,".css-1rynq56.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-18u37iz.r-1wvb978")
    for i in liste2:
        x=i.text
        if x not in divliste:
            divliste.append(x)
    yeniyukseklik=driver.execute_script("return document.documentElement.scrollHeight")
    if sonyukseklik==yeniyukseklik:
        break
    sonyukseklik=yeniyukseklik

sayac=0

for k in divliste:
    sayac+=1
    sayac=sayac
    print(f"{sayac}-{k}")


