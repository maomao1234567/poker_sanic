import requests
r = requests.get("https://zh.pokerstrategy.com/glossary")
r.encoding = 'utf-8'
print(r.text)