import scrapy
from ..items import CototestItem

class ClaroSpider(scrapy.Spider):
    name = 'claro'
    start_urls = [
        'https://www.claro.com.ar/personas/portabilidad'
    ]

    def parse(self, response):
        item = CototestItem()
        planes = response.css('div.plan-item__wrapper')

        for plan in planes:
            price = plan.css('.plan-item__price__text::text').extract()[1]
            plan_name = plan.css('strong::text').extract()
            # ejemplo para extraer un attr: response.css('.cfMarker::attr(src)')

            item['price'] = price
            item['plan_name'] = plan_name

            yield item
