# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter, PprintItemExporter
from pathlib import Path
import csv
import json


class RatingUrlsPipeline:
    def open_spider(self, spider):
        filepath = Path("data_files/urls.csv")

        self.file = open(filepath, "w", newline="")
        self.writer = csv.writer(self.file)
        self.writer.writerow(["?start=00"])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow([item["link"]])
        return item

class RatingsPipeline:
    def open_spider(self, spider):
        filepath = Path("data_files/ratings.json")
        self.file = open(filepath, "wb")
        self.exporter = JsonItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
