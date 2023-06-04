import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
images = soup.select("img")
for image in images:
 src = image.get("src")
 if src.startswith("//"):
    src = src[2:]
 elif src.startswith("/"):
    src = src[1:]
 print(src)