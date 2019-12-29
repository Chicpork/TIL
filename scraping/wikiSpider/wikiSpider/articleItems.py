from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import Article

class ArticleSpider(CrawlSpider):
    name='articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=['en.wikipedia.org/wiki/((?!:).)*$']), callback='parse_items', follow=True),]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        text_rule = '//div[@id="mw-content-text"]//text()'
        article['text'] = response.xpath(text_rule).extract()
        update_rule = 'li#footer-info-lastmod::text'
        lastUpdated = response.css(update_rule).extract_first()
        article['lastUpdated'] = lastUpdated.replace('his page was last edited on ', '')

        return article