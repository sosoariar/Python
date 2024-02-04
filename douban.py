import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header={}
header['user-agent']=user_agent

url = 'https://book.douban.com/tag/%E6%8E%A8%E7%90%86'

response = requests.get(url,headers=header)

from bs4 import BeautifulSoup as bs
bs_info = bs(response.text,'html.parser')
print(bs_info.find_all('div',attrs={'class':'info'})[0])

for tags in bs_info.find_all('div',attrs={'class':'info'}):
    for atag in tags.find_all('a',):
        print(atag.get('href'))
        print(atag.get('title'))