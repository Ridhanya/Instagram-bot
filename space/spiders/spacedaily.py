import scrapy
from ..items import SpaceItem


class SpacedailySpider(scrapy.Spider):
    name = 'spacedaily'
    next_page = None
    space_link = None
    start_urls = [
        'http://www.space.com/'
    ]

    def parse(self, response):

        if SpacedailySpider.next_page is None:
            SpacedailySpider.space_link = response.css('.article-link::attr(href)').extract()
            print(SpacedailySpider.space_link)

        for x in SpacedailySpider.space_link:
            if SpacedailySpider.next_page is not None:
                items = SpaceItem()
                space_heads = response.css('h1::text').extract()
                space_contants = response.css('p:nth-child(12) , p:nth-child(11) '
                                              ', p:nth-child(10) , p:nth-child(9) , p:nth-child(8) '
                                              ', p:nth-child(7) , p:nth-child(6) '', p:nth-child(5) '
                                              ', p:nth-child(4) , p:nth-child(3) , p:nth-child(2) '
                                              ', p:nth-child(1)').css('::text').extract()
                items['space_contants'] = space_contants
                items['space_heads'] = space_heads
                yield items
            SpacedailySpider.next_page = x
            yield response.follow(SpacedailySpider.next_page, callback=self.parse)
