from scrapy.crawler import CrawlerProcess

from grizoni.grizoni.spiders.grizoni_properties import GrizoniPropertiesSpider

process = CrawlerProcess()

# Execute Spider
process.crawl(GrizoniPropertiesSpider)
process.start()
