# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from datetime import date


class HelpDoruPipeline:
    def process_item(self, item, spider):
        return item


class DownfilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_name = 'default'
        today = date.today()
        str = today.strftime("%d/%m/%Y")
        if 'day-ahead' in request.url:
            file_name = 'AT_day-ahead_' + str
        return file_name