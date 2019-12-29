from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name='articles'
    allowed_domains = ['wikipidia.org']
    start_urls = ['https://en.wikipedia.org/wiki/'
     'Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True, cb_kwargs={'is_article':True}),
             Rule(LinkExtractor(allow='.*'), callback='parse_items', cb_kwargs={'is_article':False})]

    def parse_items(self, response, is_article):
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was last edited on ', '')
        print('URL is : {}'.format(url))
        print('Title is: {}'.format(title))
        print('text is: {}'.format(text))
        print('Last updated is: {}'.format(lastUpdated))

    def parse_items(self, response, is_article):
        print(response.url)
        title = response.css('h1::text').extract_first()

        if is_article:
            url = response.url
            text_rule = '//div[@id="mw-content-text]//text()'
            text = response.xpath(text_rule).extract()

            update_rule = 'li#footer-info-lastmod::text'
            update_delete = 'This page was last edited on '
            lastUpdated = response.css(update_rule).extract_first()
            lastUpdated = lastUpdated.replace(update_delete, '')

            print('Title is: {}'.format(title))
            # print('URL is : {}'.format(url))
            print('last updated: {}'.format(lastUpdated))
            print('text is: {}'.format(text))
        else:
            print('This is not an article: {}'.format(title))
