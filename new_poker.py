import requests
from bs4 import BeautifulSoup
import json


def get_html(url):
    try:
        headers = {
            'User-Agent': 'Chrome/63.0.3239.26'
        }
        reponse = requests.get(url, headers=headers)
        reponse.raise_for_status()
        return reponse.text
    except:
        return '请求错误'


def parse_html(text):
    soup = BeautifulSoup(text, 'lxml')
    urla = soup.select('.content_a a')
    allul = []
    for ur in urla:
        allul.append(ur['href'])
    for href in allul:
        newurl = 'http://thepokerlogic.com' + str(href)     #拼接后的链接
        data = requests.get(newurl).text                    #获取子页html代码
        soup1 = BeautifulSoup(data, 'lxml')
        allh2 = soup1.select('.glossary-detail-title')
        allh3 = soup1.find_all('h3')
        allp = soup1.find_all('p')
        allh4 = soup1.find_all('h4')
        if len(allh2) == 0:
            pass
        else:
            title = allh2[0].string             #大标题
        concept1 = soup1.select('.relevant-content a')
        if len(concept1) == 0:
            concept_cont = '无'
        else:
            for i in concept1:
                concept_cont = i.string

        study1 = soup1.select('.study-content a')
        if len(study1) == 0:
            study_cont = '无'
        else:
            for i in study1:
                study_cont = i.string

        ctitle = allh3[0].string            # 汉字大标题
        title_explain = allp[4].string      # 标题解释
        example = allh4[0].string           # 举例说明
        exa_cont = allp[5].string           # 说明的内容
        concept = allh4[1].string           # 相关概念


        result = {
            'English_title': title,
            'Chinese_title': ctitle,
            'Title_explain': title_explain,
            'Illustrate': example,
            'Illustrate_content': exa_cont,
            'Concept': concept,
            'Concept_content': concept_cont,
            'Study_content': study_cont,
        }
        write_file(result)


def write_file(data1):
    with open('result.json', 'a', encoding='utf-8')as file:
        file.write('\n' + json.dumps(data1, ensure_ascii=False))


def main():
    url = 'http://thepokerlogic.com/glossary'
    text = get_html(url)
    parse_html(text)


main()
