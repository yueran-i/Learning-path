import requests
from bs4 import BeautifulSoup
import time
keyword = "怎么做饭"
max_page = 5
wait_time = 1
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/123.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
    "Referer": "https://www.baidu.com/", 
    "Connection": "keep-alive" 
}
for page in range(max_page):
    current_pn = page*10
    print(f"正在爬第{page+1}页")
    params = {"wd":keyword,"pn":current_pn}
    try:
        response = requests.get("https://www.baidu.com/s",params=params,headers=headers,timeout=10)
        response.raise_for_status()
    except Exception as error:
        print(f"第{page+1}页爬取失败，错误：{error}")
        continue
    response.encoding = "utf-8"
    htlm = response.text
    soup = BeautifulSoup(htlm,"html.parser")
    results = soup.find_all("div",class_="result")
    if not results:
        print(f"第{page+1}无搜索结果，有可能被反爬了")
        continue
    for index,result in enumerate(results):
        title_tag = result.find("h3")
        if title_tag :
            title = title_tag.get_text()
        a_tag = result.find("a")
        if a_tag :
            link = a_tag["href"]
            print(f"{index+1}.标题：{title}")
            print(f"  链接：{link}\n===========")
    time.sleep(wait_time)
print("所有页面爬取完成")