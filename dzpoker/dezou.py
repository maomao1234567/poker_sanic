import requests
import json
from bs4 import BeautifulSoup

def gethtmltext(url):
    """
    param url:传入地址
    对传入地址进行解析，提取
    """
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        #伪装
        r=requests.get(url,timeout=30,headers=kv)
        # 获取源码
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        #判断是否成功，修改编码方式未UTF-8
        demo=r.text
        soup=BeautifulSoup(demo,"html.parser")
        return soup
    except:
        return "产生异常"

def extract(soup):
    """
    param soup:传入BeautifulSoup对象
    通过嵌套 遍历 查找所需内容
    """
    soup4 = soup.find_all('h2')
    soup2 = soup.find_all('h3')
    soup3 = soup.find_all('p')
    jj=''
    ss=[]
    hh=[]
    str2=[]
    str3=[]
    for i in soup.find_all('div', class_="detail-illustrate"):
        for j in i.find_all('p'):
            jj=j.string
        for j in i.find_all('a'):
            jj=j.string
    for j in soup.find_all('div', class_="detail-relevant"):
        m=0
        for i in j.find_all('div',class_="relevant-content"):
          if i.find_all('p')!=[]:
            for s in i.find_all('p'):
               ss.insert(m,s.string)
               if s.get('href')!=None:
                 str2.insert(m,s.get('href'))
               m+=1
          else:
             for s in i.find_all('a'):
               ss.insert(m,s.string)
               if s.get('href') != None:
                 str2.insert(m,s.get('href'))
               m+=1
    for j in soup.find_all('div', class_="detail-study"):
       for i in j.find_all('div',class_="study-content"):
         m=0
         if i.find_all('p')!=[]:
            for h in i.find_all('p'):
               hh.insert(m,h.string)
               if h.get('href') != None:
                 str3.insert(m,h.get('href'))
               m+=1
         else:
            for h in i.find_all('a'):

               hh.insert(m,h.string)
               if h.get('href') != None:
                 str3.insert(m,h.get('href'))
               m+=1

    data = {
        'name': soup4[0].string,
        'introduce': soup2[0].string,
        'detail': soup3[4].string,
        'example':jj,
        'concept':ss,
        'concept-href': str2,
        'study':hh,
        'study-href': str3,
         } #创建字典并赋值
    if len(data['concept-href']) ==0:
        data['concept-href']='无'
    if len(data['study-href'])==0:
        data['study-href']='无'
    write(data)#调用写入函数

def write(data):
    """
    param data: 传入字典
    调用json方法将字典写入文本

    """
    s_ = json.dumps(data,ensure_ascii =False) #将编码形式修改为UTF-8,避免读入乱码
    with open('/home/leisongbai/桌面/111.json','a') as f:
        f.write(s_)



def body(str):

    url="http://thepokerlogic.com"+str
    soup=gethtmltext(url)
    extract(soup)





