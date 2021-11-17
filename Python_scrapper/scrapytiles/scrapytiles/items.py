# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def replace_tm(string):
    return string.replace("®", "").replace("™", "")


class ScrapytilesItem(scrapy.Item):
    Name = scrapy.Field(input_processor=MapCompose(remove_tags, replace_tm),
                        output_processor=TakeFirst())
    Price = scrapy.Field(input_processor=MapCompose(remove_tags),
                         output_processor=TakeFirst())
    Sku = scrapy.Field(output_processor=TakeFirst())
