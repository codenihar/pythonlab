import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top"
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
movies = soup.select(".titleColumn a")
for movie in movies[:10]:
 link = "https://www.imdb.com" + movie.get("href")
 movie_response = requests.get(link, headers=headers)
 if movie_response.ok:
    soup = BeautifulSoup(movie_response.content, "html.parser")
 # Extract movie name
 try:
    movie_name = soup.select_one('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO > section > div:nth-child(4) > section > section > div.scab3b6b3d-3.goiwap > div.sc-2971dade-0.YVoIO > h1 > span').text.strip().split(" (")[0]
 except AttributeError:
    movie_name = "N/A"
 # Extract movie year
 try:
    movie_year = soup.select_one('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO > section > div:nth-child(4) > section > section > div.scab3b6b3d-3.goiwap > div.sc-2971dade-0.YVoIO > ul > li:nth-child(1) > a').text.strip()
 except AttributeError:
    movie_year = "N/A"
 # Extract movie summary
 try:
    movie_summary = soup.select_one('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO > section > div:nth-child(4) > section > section > div.scab3b6b3d-4.fzQBuI > div.sc-ab3b6b3d-6.cbFSCE > div.sc-ab3b6b3d10.kreISa > section > p > span.sc-35061649-0.fjlUgo').text.strip()
 except AttributeError:
    movie_summary = "N/A"
 print(f"Name: {movie_name}")
 print(f"Year: {movie_year}")
 print(f"Summary: {movie_summary}")
 print("--------------------")
