from bs4 import BeautifulSoup
import requests
r = requests.get('https://zh.pokerstrategy.com/glossary').content
resolver = BeautifulSoup(r, 'html.parser')
links = resolver.findAll('a')
for link in links:
    print(link)

