import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader

from follow_links.follow_links.items import FollowLinksItem


class FollowSpider(scrapy.Spider):
    name = 'follow'
    allowed_domains = ['fake-plants.co.uk']
    start_urls = ['http://www.fake-plants.co.uk']

    def parse(self, response, **kwargs):
        for link in response.css("li.product-category a::attr(href)"):
            yield response.follow(link.get(), callback=self.parse_categories)

    def parse_categories(self, response):
        products = response.css("div.astra-shop-summary-wrap")
        for product in products:
            l = ItemLoader(item=FollowLinksItem(), selector=product)

            l.add_css("Category", "span.ast-woo-product-category")
            l.add_css("Name", "h2.woocommerce-loop-product__title")
            l.add_css("Link", "a::attr(href)")

            yield l.load_item()


process = CrawlerProcess(settings={
    "FEED_URI": "../../plants.css",
    "FEED_FORMAT": "csv"
})
process.crawl(FollowSpider)
process.start()
