import scrapy

from ..items import DownfilesItem


class CeghDayCSVAheadSpider(scrapy.Spider):
    name = "cegh_dayahead_csv"
	
    def start_requests(self):
        url = 'https://www.cegh.at/wp-admin/admin-ajax.php'
        form_data={
            'action': 'get_DayAheadMarket',
            'product': 'aheadMarket',
            'market': 'AT'
        }
        
        yield scrapy.FormRequest(url,
                                 formdata=form_data)

    def parse(self, response):
        file_url = response.css('a[class="ce-table__button btn btn--secondary btn--icon btn--icon--download exportButton"]').get()
        file_url = response.urljoin(file_url)
        item = DownfilesItem()
        item['file_urls'] = [file_url]
        item['original_file_name'] = file_url.split('/')[-1]
        yield item