import requests
from bs4 import BeautifulSoup
params = {"wd": "python"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/123.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
    "Referer": "https://www.baidu.com/", 
    "Connection": "keep-alive" 
}
response = requests.get("https://www.baidu.com/s",params=params,headers=headers)
print("最终请求的网址：",response.url)
response.encoding = "utf-8"
htlm = response.text
soup = BeautifulSoup(htlm,"html.parser")
results = soup.find_all("div",class_="result")
for result in results:
    title_tag = result.find("h3")
    if title_tag :
        title = title_tag.get_text()
    a_tag = result.find("a")
    if a_tag :
        link = a_tag["href"]
        print("标题：",title)
        print("链接：",link)
