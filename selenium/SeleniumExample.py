from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service




options = Options()

options.add_experimental_option("excludeSwitches",["enable-logging"])
service=Service("{YourDriverPath}")
driver = webdriver.Chrome(service=service,options=options)

url="https://www.idefix.com/"


driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(3)
kitap=driver.find_element("xpath", "//*[@id='__next']/header/div[2]/ul/li[1]/div/a").click()
arama=driver.find_element("xpath", "//*[@id='headerSearch-d']")
arama.send_keys("şiir")
arama.send_keys(Keys.ENTER)

for i in range(1,10):
    bilgi=driver.find_element("xpath","//*[@id='__next']/div[5]/div/div/div[2]/section/div[{}]/div[2]/p".format(i))##yanlış xpath olduğu için sayfadakileri görüntüleyemedi
    print(bilgi.text)

driver.close()






### Eksisözlük giriş ve arama
# time.sleep(3)
# # debe=driver.find_element("xpath", "//*[@id='quick-index-nav']/li[2]/a").click()
# arama=driver.find_element("xpath", "//*[@id='search-textbox']")
# arama.send_keys("şiir")
# button=driver.find_element("xpath", "//*[@id='search-form']/button").click()
# # arama.send_keys(Keys.ENTER) da olabilir click yerine
# time.sleep(5)


















#İLK SELENIUM DERSİYDİ
# from selenium import webdriver
# import time


# driver = webdriver.Chrome()

# url="https://youtube.com/"

# driver.get(url)
# print(driver.page_source)
# driver.close()
