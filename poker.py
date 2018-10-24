from bs4 import BeautifulSoup
import requests


def get_html(url):
    '''获取网页的html代码'''
    data = requests.get(url)
    data.encoding = 'utf-8'
    return data


def analyze_data(data):
    '''分析代码'''
    soup = BeautifulSoup(data.text, 'lxml')
    text = soup.select('.content-list-box .content_name')
    return text


def save_result(text):
    '''保存数据'''
    with open('result.json', 'w') as file:
        for re in text:
            file.write(re.string)


def main():
    url = 'http://thepokerlogic.com/glossary'
    data = get_html(url)
    text = analyze_data(data)
    save_result(text)


main()