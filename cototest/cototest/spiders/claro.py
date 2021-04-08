import scrapy

class ClaroSpider(scrapy.Spider):
    name = 'claro'
    start_urls = [
        'https://www.claro.com.ar/personas/portabilidad'
    ]

    def parse(self, response):
        planes = response.css('div.plan-item__wrapper')

        for plan in planes:
            price = plan.css('span.plan-item__price__text::text').extract()
            plan_name = plan.css('span.plan-item__title::text').extract()
            yield dict(price=price, plan_name=plan_name)