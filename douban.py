import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header={}
header['user-agent']=user_agent

url = 'https://book.douban.com/tag/%E6%8E%A8%E7%90%86'

response = requests.get(url,headers=header)

print(response.text)
