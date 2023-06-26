import scrapy

from ..items import TradingItem


class CeghDayCSVAheadSpider(scrapy.Spider):
    name = "cegh_dayahead_csv"
	
	start_urls = [
        "https://www.cegh.at/wp-admin/admin-ajax.php?action=exportPosts&postType=day-ahead&market=AT",
    ]
    
    def parse(self, response):
        print('done page')
        
