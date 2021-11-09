# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def remove_currency(value):
    return value.replace("£", "").strip()


class WhiskyItem(scrapy.Item):
    # This take item["name"] than remove tags and then takes non-None value
    name = scrapy.Field(input_processor=MapCompose(remove_tags),  # MapCompose is used to execute function in code
                        output_processor=TakeFirst())  # Returns the first non-None value or returns nothing
                                                       # If there are only Nones

    # Actually does the same as with "name" but we added our oun function
    price = scrapy.Field(input_processor=MapCompose(remove_tags, remove_currency),
                         output_processor=TakeFirst(),
                         )
    link = scrapy.Field()
