# import scrapy
#
# class StoreSpider(scrapy.Spider):
#     name = "stores"
#
#     def start_request(self):
#         urls = [
#             'https://www.apple.com/retail/storelist/'
#         ]
#
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'apple %s' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)


import scrapy


class StoreSpider(scrapy.Spider):
    name = "stores"

    def start_requests(self):
        urls = [
            'https://www.apple.com/retail/storelist/'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'apple-%s.json' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)