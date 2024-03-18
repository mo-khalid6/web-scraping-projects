import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RadioInfoSpider(CrawlSpider):
    name = "radio_info"
    allowed_domains = ["mytuner-radio.com"]
    start_urls = ["https://mytuner-radio.com/radio/"]

    rules = (Rule(LinkExtractor(restrict_xpaths="//div/ul/li/a[@class='no-select']"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        if 'radio' in response.url:


            yield{
                "Name":response.xpath("//div[@class='radio-player']/div/h1/text()").get(),
                "Country":response.xpath("//div/ul[@class='breadcrumbs']/li[1]/a/text()").get(),
                "Frequencies":response.xpath("//div[@class='frequencies']/ul/li/div/text()").getall(),
                "Genres":response.xpath("//div[@class='genres']/a/text()").getall(),
                "radio_link":response.url

            }