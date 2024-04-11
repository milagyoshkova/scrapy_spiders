# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import re

class BrosbgSpider(scrapy.Spider):
    name = 'brosbg'
    allowed_domains = ['brosbg.com']
    start_urls = ['https://brosbg.com/']

    def parse(self, response):
       
        category_links = response.xpath('//div[@class="sidebar-box-content"]//a/@href').getall()

        for category_link in category_links:
            yield response.follow(category_link, callback=self.parse_category)

    def parse_category(self, response):
       
        products = response.xpath('//div[@class="product-info"]')
        
        for product in products:
            model = product.xpath('.//h5/a/span[2]/text()').get()
            product_type = product.xpath('.//h5/a/span[1]/text()').get().strip()
            price_element = product.xpath('.//span[@class="price"]')
            price_text = ' '.join(price_element.xpath('.//text()').getall())
            prices = [int(price) for price in re.findall(r'\d+', price_text)]
            old_price = prices[0] if prices else None
            new_price = prices[1] if len(prices) > 1 else None
            product_url = response.urljoin(product.xpath('.//a[@itemprop="url"]/@href').get())
            product_image_url = response.urljoin(product.xpath('.//a[@itemprop="url"]/img/@src').get())

            yield {
                'model': model.strip() if model else None,
                'product_type': product_type,
                'old_price': old_price,
                'new_price': new_price,
                'product_image_url': product_image_url,
                'url': product_url,
                'category': response.url
            }

        
        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_category)
