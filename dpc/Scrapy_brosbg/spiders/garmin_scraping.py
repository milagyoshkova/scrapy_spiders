import scrapy

class GarminProductsSpider(scrapy.Spider):
    name = 'garmin_products'
    start_urls = ['https://garmin.bg/%D0%9A%D0%BE%D0%B3%D0%B0%D1%82%D0%BE-%D1%81%D1%82%D0%B5-%D0%BD%D0%B0-%D0%BF%D1%8A%D1%82%D1%8F/%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%BD%D0%B8-%D0%BD%D0%B0%D0%B2%D0%B8%D0%B3%D0%B0%D1%82%D0%BE%D1%80%D0%B8-Drive']

    def parse(self, response):
        products = response.xpath('//*[@id="products"]/div/div/div/div')

        for product in products:
            product_title = product.xpath('.//h6/a/text()').get()
            price = product.xpath('.//span[@class="price-new"]/text()').get()
            image_url = product.xpath('.//div[@class="image"]/a/img/@src').get()

            yield {
                'product_title': product_title.strip() if product_title else 'No title available',
                'price': price.strip() if price else 'Price not available',
                'image_url': image_url if image_url else 'Image link not found'
            }
