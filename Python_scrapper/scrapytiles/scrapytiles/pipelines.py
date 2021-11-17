# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting !!!!!!!!!
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html !!!!!!!!
# Lines 64-66


# useful for handling different item types with a single interface
import sqlite3


class ScrapytilesPipeline:
    def __init__(self):
        self.con = sqlite3.connect("mtiles.db")  # Name of data base
        self.cur = self.con.cursor()  # Is what we use to execute commands on database
        self.create_table()

    def create_table(self):  # Create table if it is not already exist
        self.cur.execute("""CREATE TABLE IF NOT EXISTS products(    
        sku REAL PRIMARY KEY,
        name TEXT,
        price REAL
        )""")  # Says that sku is real number and makes it like id

    def process_item(self, item, spider):  # Item is actual item from the spider
        self.cur.execute("""INSERT OR IGNORE INTO products VALUES (?,?,?)""",
                         (item["Sku"], item["Name"], item["Price"]))  # To avoid duplicate
        # ? is for each field in item
        self.con.commit()
        return item
