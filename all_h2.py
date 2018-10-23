from bs4 import BeautifulSoup
import requests


def get_html(url):
    data = requests.get(url)
    data.encoding = 'utf-8'
    return data


def analysis(data):
    soup = BeautifulSoup(data.text, 'xml')
    text = soup.find_all('div', class_='content_a')
    return text


def display(text):
    for txt in text:
        print(txt.text, end=" ")


def main():
    url = 'http://thepokerlogic.com/glossary'
    data = get_html(url)
    text = analysis(data)
    display(text)


main()
