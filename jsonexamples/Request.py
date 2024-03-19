import requests
import json


site=requests.get("https://jsonplaceholder.typicode.com/todos")
cevap=json.loads(site.text)

for i in cevap:
    print(i)