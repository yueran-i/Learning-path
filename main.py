import requests
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
print("输出的内容",response.text)
