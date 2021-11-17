import scrapy
from scrapy.loader import ItemLoader

from ..items import ScrapytilesItem


class TilesSpider(scrapy.Spider):
    name = 'tiles'
    allowed_domains = ['magnatiles.com']
    start_urls = ['https://www.magnatiles.com/products/page/1']

    def parse(self, response, **kwargs):
        products = response.css("ul.products li")
        for item in products:
            l = ItemLoader(item=ScrapytilesItem(), selector=item)

            l.add_css("Name", "h2")
            l.add_css("Price", "bdi")
            l.add_css("Sku", "a.button::attr(data-product_sku)")

            yield l.load_item()

        next_page = response.css("a.next.page-numbers::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
