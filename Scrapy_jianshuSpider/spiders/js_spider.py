# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Scrapy_jianshuSpider.items import ArticleItem


class JsSpiderSpider(CrawlSpider):
    name = 'js_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
        # 通过对url分析，文章id是由0-9数字和a-z小写字母组成。正则表达式里面.*表示可有可无
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get()
        # 分析url得到两种形式：
        # https://www.jianshu.com/p/a0199fe1507c?utm_campaign=maleskine&utm_content=note&utm_medium=pc_all_hots&utm_source=recommendation
        # https://www.jianshu.com/p/a0199fe1507c
        origin_url = response.url
        # url被问号？分割后返回一个列表['https://www.jianshu.com/p/a0199fe1507c', 'utm_campaign=maleskine&utm_content=note&utm_medium=pc_all_hots&utm_source=recommendation']
        # 或者得到列表['https://www.jianshu.com/p/a0199fe1507c']
        url = origin_url.split('?')[0]
        article_id = url.split('/')[-1]
        # 文章内容，包括所有的html标签，而不是纯文本信息
        content = response.xpath("//div[@class='show-content-free']").get()

        item = ArticleItem(
            title = title,
            content = content,
            avatar = avatar,
            author = author,
            pub_time = pub_time,
            origin_url = origin_url,
            article_id = article_id
        )
        yield item

