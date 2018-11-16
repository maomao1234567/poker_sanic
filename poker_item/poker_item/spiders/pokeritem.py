import scrapy
from scrapy.spiders import Spider
from poker_item.items import PokerItemItem


class PokeritemSpider(Spider):

    #爬虫名
    name = 'pokeritem'
    #限制网站
    allowed_domains = ['zh.pokerstrategy.com']
    #初始网站
    start_urls = ['https://zh.pokerstrategy.com/glossary/']
    #用于保存每个name属性
    list = {}
    #计数器
    j = 0

    def parse(self, response):
        #获取所有的链接
        list_url = response.xpath('//div[@class="glossarySection--list"]/ul/li//a/@href').extract()
        #获取所有的name
        list_name = response.xpath('//div[@class="glossarySection--list"]/ul/li//a/text()').extract()
        n = len(list_url)
        h = 0
        while h < n:
            PokeritemSpider.list['https://zh.pokerstrategy.com'+list_url[h]]=list_name[h]
            h += 1
        #通过遍历爬取每一个链接
        for li in list_url:
            yield scrapy.Request('https://zh.pokerstrategy.com'+li,callback=self.parse_item,dont_filter=True)

    def parse_item(self, response):
        print(response)
        #创建字典，用于保存内容
        item = PokerItemItem()
        #获取div中的全部信息
        string = response.xpath("//*[@id='fullBody2']/div/section/section/div//text()").extract()
        #给item的头赋值
        item['name'] = PokeritemSpider.list[response.url]
        #将string的第一个数据作为头
        item['head'] = string[1].strip()
        #使用循环将string列表的其余部分连接起来
        n = len(string)
        str = ''
        i = 2
        while i < n:
            str =str + string[i]
            i+=1
        item['body'] = str
        #用空格将\r\n\t替换
        item['body'] = item['body'].replace('\r', '').replace('\n', '').replace('\t', '')
        #删去多余的空格
        item['body'] = item['body'].strip()
        #计数器加
        PokeritemSpider.j += 1
        #返回字典，并通过pipline保存
        yield item
