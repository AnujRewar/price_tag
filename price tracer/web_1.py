import requests
from bs4 import BeautifulSoup
class PriceTracer:
    def __init__(self,url):
        self.url=url
        self.user_agent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
        self.response=requests.get(url=self.url,headers=self.user_agent).text
        self.soup=BeautifulSoup(self.response,"lxml")
    def product_title(self):
        title=self.soup.find("span",class_="VU-ZEz")
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"
    def product_price(self):
        price=self.soup.find("span",class_="Nx9bqj.CxhGGd")
        if price is not None:
            return price.text.strip()
        else:
            return "Tag not found"
        
device=PriceTracer(url="https://www.flipkart.com/hp-15s-athlon-dual-core-4-gb-1-tb-hdd-windows-10-home-15s-gy0001au-thin-light-laptop/p/itmfde60f9520336?pid=COMGFHGFZ7HFZSBA&lid=LSTCOMGFHGFZ7HFZSBAUX64XI&marketplace=FLIPKART&q=hp+15+da0411tu&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&fm=SEARCH&iid=55bfc5fd-c3a1-4d54-9f48-7a5b0263dd97.COMGFHGFZ7HFZSBA.SEARCH&ppt=browse&ppn=browse&ssid=xynw70i94g0000001624006466851&qH=8d56cf21d8e26394")
print(device.product_title())
print(device.product_price())