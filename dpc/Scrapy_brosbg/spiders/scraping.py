import scrapy


class ScrapingSpider(scrapy.Spider):
    name = "scraping"
    allowed_domains = ["brosbg.com"]
    start_urls = ["http://brosbg.com/"]

    def parse(self, response):
        pass
