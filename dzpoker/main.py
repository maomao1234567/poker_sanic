import dezou
def circul(soup):
    """
    :param soup:首页地址
    通过循环调用，将所有页面依次爬取
    """
    for i in soup.find_all(class_="glossary-content"):
        for j in i.find_all('a'):
            dezou.body(j.get('href'))


url1="http://thepokerlogic.com/glossary"
soups=dezou.gethtmltext(url1)
circul(soups)

