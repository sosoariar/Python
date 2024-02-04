import requests

url = 'https://book.douban.com/tag/%E6%8E%A8%E7%90%86'

response = requests.get(url)

print(response)