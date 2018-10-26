import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from poker_item.items import PokerItemItem


class PokeritemSpider(CrawlSpider):

    name = 'pokeritem'
    allowed_domains = ['thepokerlogic.com']
    start_urls = ['http://thepokerlogic.com/glossary']

    rules = (Rule(
        LinkExtractor(
            allow=r'.html$', restrict_xpaths='//div[@class="content_a"]/a'),
        callback='parse_item',
        follow=True), )

    def parse_item(self, response):
        item = PokerItemItem()

        item['name'] = response.xpath(
            '//h2[@class="glossary-detail-title"]/text()').extract_first()
        item['trans'] = response.xpath(
            '//div[@class="detail-describe"]/h3/text()').extract_first()
        item['define'] = response.xpath(
            'normalize-space(//div[@class="describe-content"]/p/text())'
        ).extract_first()
        item['example'] = response.xpath(
            '//div[@class="illustrate-content"]/p/text()').extract_first()

        relevant_content_a = response.xpath(
            '//div[@class="relevant-content"]/a/text()').extract_first()
        relevant_content_p = response.xpath(
            '//div[@class="relevant-content"]/p/text()').extract_first()
        if not relevant_content_a:
            item['concept'] = relevant_content_p
        else:
            item['concept'] = relevant_content_a

        study_content_a = response.xpath(
            '//div[@class="study-content"]/a/text()').extract()
        study_content_p = response.xpath(
            '//div[@class="study-content"]/p/text()').extract()
        if not study_content_a:
            item['study'] = study_content_p
        else:
            item['study'] = study_content_a

        yield item
