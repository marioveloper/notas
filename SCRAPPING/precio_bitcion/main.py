import requests
from bs4 import BeautifulSoup
from config import *

def precio_Bitcoin(url):

    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers=headers, timeout=20)

    if req.status_code != 200:
        return {"ERROR" : f"{req.reason}", "status_code" : f"{req.status_code}"}

    soup = BeautifulSoup(req.text, "html.parser")
    bitcoin = soup.find("span", class_="pclqee").text
    return bitcoin

if __name__=="__main__":
    print(precio_Bitcoin(URL))