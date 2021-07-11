import requests
from bs4 import BeautifulSoup
import json
import pprint
import os 
url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
data1=requests.get(url)
soup = BeautifulSoup(data1.text,'html.parser')
no=soup.find("div",class_="_1EI9")
serial=no.span.get_text()
split=serial.split()
p=split[1]
pr=int(p)//32+1
serial_no=1
j=1
pickle=[]
while j<=pr:
    Url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(j)
    Data1=requests.get(Url)
    Soup = BeautifulSoup(Data1.text,'html.parser')
    diV1=Soup.find("div",class_="_3RA-")
    diV2=diV1.find_all("div",class_="UGUy")
    diV3=diV1.find_all("div",class_="_1kMS")
    diV4=diV1.find_all("div",class_="_3WhJ")
    i=0
    while i<len(diV1):
        pickle_name=diV2[i].get_text()
        pickle_rate=diV3[i].get_text()
        pickle_link=diV4[i].a["href"]
        url1="https://paytmmall.com"+pickle_link
        de={"position":"","name":"","price":"",'url':""}
        de["position"]=serial_no
        de["name"]=pickle_name
        de["price"]=pickle_rate
        de["url"]=url1
        pickle.append(de.copy())
        serial_no+=1
        i+=1
    j+=1
with open("TASK1.json","w") as f:
    json.dump(pickle,f,indent=3)

