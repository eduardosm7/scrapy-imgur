import scrapy
from Imgur.items import ImgurItem


class ImgurSpider(scrapy.Spider):
    name = 'imgur'

    def start_requests(self):
        yield scrapy.Request('https://imgur.com/search?q=' + self.arg)

    def parse(self, response):
        image = ImgurItem()
        rel = response.xpath("//img/@src").extract()
        image['image_urls'] = ['http:' + rel[0]]
        return image
