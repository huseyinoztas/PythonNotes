from instaBilgi import kullaniciAdi,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_experimental_option("excludeSwitches",["enable-logging"])
service=Service("{YourDriverPath}")
driver = webdriver.Chrome(service=service,options=options)
url="https://www.instagram.com"

driver.get(url)
time.sleep(5)
ka=driver.find_element("xpath","//*[@id='loginForm']/div/div[1]/div/label/input")
ka.send_keys(kullaniciAdi)
sif=driver.find_element("xpath","//*[@id='loginForm']/div/div[2]/div/label/input")
sif.send_keys(sifre)
sif.send_keys(Keys.ENTER)
time.sleep(2)
driver.maximize_window()
time.sleep(5000)
