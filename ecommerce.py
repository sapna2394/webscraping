from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json

def Ecomerce():
    Ecomerce_api='https://webscraper.io/test-sites'
    Ecomerce_url=requests.get(Ecomerce_api)
    Text_data=Ecomerce_url.json
    soup=BeautifulSoup(Ecomerce_url.text,"html.parser")
    name = soup.find_all("h2")
    number=0
    list=[]
    for i in name:
        number += 1
        url = i.find("a")["href"]
        name = i.find("a").get_text().strip()
        Ecomerce_dict={'position':number,'Ecomerce_name':name,'Ecomerce_url':"https://webscraper.io"+url}
        list.append(Ecomerce_dict)
        with open("Ecomerce.json",'w') as f:
            json.dump(list,f,indent = 4)
    return (list)
Ecomerce()