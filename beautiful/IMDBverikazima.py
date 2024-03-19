import requests
from bs4 import BeautifulSoup


link="https://www.imdb.com/chart/top/"

kod=requests.get(link,headers={'User-Agent': 'Mozilla/5.0'}).content

parser=BeautifulSoup(kod,"html.parser")
li=parser.find("ul",{"class":"ipc-metadata-list ipc-metadata-list--dividers-between sc-71ed9118-0 kxsUNk compact-list-view ipc-metadata-list--base"}).find_all("li")

for i in li:
    baslik=i.find("div",{"class":"ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title"}).find("a").string
    
    print(baslik)