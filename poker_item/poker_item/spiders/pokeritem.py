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
    list_name = []
    #计数器
    j = 0

    def parse(self, response):
        #获取所有的链接
        list_url = response.xpath('//div[@class="glossarySection--list"]/ul/li//a/@href').extract()
        #获取所有的name
        PokeritemSpider.list_name = response.xpath('//div[@class="glossarySection--list"]/ul/li//a/text()').extract()
        #通过遍历爬取每一个链接
        for li in list_url:
            yield scrapy.Request('https://zh.pokerstrategy.com'+li,callback=self.parse_item)

    def parse_item(self, response):

        #创建字典，用于保存内容
        item = PokerItemItem()
        item['name'] = PokeritemSpider.list_name[PokeritemSpider.j]
        item['body'] = response.xpath("//*[@id='fullBody2']/div/section/section/div//text()").extract()
        #计数器加1
        PokeritemSpider.j += 1
        #返回字典，并通过pipline保存
        yield item
