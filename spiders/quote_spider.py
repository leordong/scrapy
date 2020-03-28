import scrapy
from ..items import AmazonSpiderItem

class quote_spider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1585354544&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]

    def parse(self, response):

        items = AmazonSpiderItem()

        title = response.css('.a-color-base.a-text-normal::text').extract()
        author = response.css('.a-color-secondary .a-size-base+ .a-size-base::text').extract()
        price = response.css('.a-spacing-top-small .a-price-whole::text').extract()

        items['title'] = title
        items['author'] = author
        items['price'] = price

        yield items