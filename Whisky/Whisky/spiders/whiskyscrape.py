import scrapy
from Whisky.items import WhiskyItem  # This path is from current file
from scrapy.loader import ItemLoader

# It is normally that PyCharm marks this like error

class WhiskyscrapeSpider(scrapy.Spider):
    name = 'whiskyscrape'
    allowed_domains = ['whiskyshop.com']
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response, **kwargs):
        for product in response.css("div.product-item-info"):
            l = ItemLoader(item=WhiskyItem, selector=product)  # Sends the data for the Loadr

            l.add_css("name", "a.product-item-link")
            l.add_css("price", "span.price")
            l.add_css("link", "a.product-item-link::attr(href)")

            # item["name"] = product.css("a.product-item-link::text").get()
            # item["price"] = product.css("span.price::text").get()
            # item["link"] = product.css("a.product-item-link").attrib["href"]

            yield l.load_item()

        next_page = response.css("a.action.next").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
