# Scrapy_jianshuSpider
【Scrapy框架实战】简书网整站爬虫</br>
</br>
功能点如下(持续补充)↓：</br>
1.使用Scrapy框架</br>
2.使用Crawl Spider爬虫对相同规则结构url进行爬取
3.将爬取下来的数据保存到MySQL数据库中</br>
4.改进数据保存方式，采用twisted异步保存到MySQL</br>
5.自定义DownloadMiddleware下载器中间件，将Selenium + Chromedriver集成到Scrapy中模拟浏览器行为爬取动态网页</br>
6.实现整站爬取</br>
</br>
</br>
项目主要截图↓：</br>
</br>
需要爬取的简书网文章列表页，“阅读更多”需要ajax异步加载，则需要使用Selenium+Chromedriver实现爬取↓</br>
![ScreenShot 1](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/1.%E7%AE%80%E4%B9%A6%E7%BD%91%E6%95%B4%E7%AB%99%E7%88%AC%E8%99%AB.png)      
</br>
</br>
自动爬取页面，见“Chrome正受到自动测试软件的控制”，Selenium+Chromedriver已经实现↓</br>
![ScreenShot2](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/2.%E8%87%AA%E5%8A%A8%E7%88%AC%E5%8F%96%E9%A1%B5%E9%9D%A21.png)      
</br>


