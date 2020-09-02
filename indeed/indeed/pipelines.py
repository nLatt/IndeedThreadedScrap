# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pathlib import Path
import csv


class IndeedPipeline:
    def open_spider(self, spider):
        filename = Path("indeed/data_files/urls.csv")
        self.file = open(filename, "w", newline="")
        writer = csv.writer(self.file)
        writer.writerow(["?start=00"])


    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        writer = csv.writer(self.file)
        writer.writerow([item["link"]])
        return item
