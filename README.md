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
</br>
1.需要爬取的简书网文章列表页，“阅读更多”需要ajax异步加载，则需要使用Selenium+Chromedriver实现爬取↓</br>
</br>
![ScreenShot 1](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/1.%E7%AE%80%E4%B9%A6%E7%BD%91%E6%95%B4%E7%AB%99%E7%88%AC%E8%99%AB.png)      
</br>
</br>
2.自动爬取页面，见“Chrome正受到自动测试软件的控制”，Selenium+Chromedriver已经实现↓</br>
</br>
![ScreenShot 2](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/2.%E8%87%AA%E5%8A%A8%E7%88%AC%E5%8F%96%E9%A1%B5%E9%9D%A21.png)      
</br>
</br>
3.文章末尾，推荐的“文章主题”，Selenium+Chromedriver模拟浏览器行为↓</br>
</br>
![ScreenShot 3](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/3.%E8%87%AA%E5%8A%A8%E7%88%AC%E5%8F%96%E9%A1%B5%E9%9D%A22.png)      
</br>
</br>
4.文章末尾，推荐的“文章主题”，Selenium+Chromedriver模拟浏览器行为↓</br>
</br>
![ScreenShot 4](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/4.%E8%87%AA%E5%8A%A8%E7%88%AC%E5%8F%96%E9%A1%B5%E9%9D%A23.png)      
</br>
</br>
5.项目结构，以及console控制台输出运行结果↓</br>
</br>
![ScreenShot 5](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/5.%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84.png)      
</br>
</br>
6.运用Scrapy Shell进行测试↓</br>
</br>
![ScreenShot 6](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/6.Scrapy%20Shell%201.png)      
</br>
</br>
7.运行Scrapy Shell对获取items的xpath语法进行测试↓</br>
</br>
![ScreenShot 7](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/7.Scrapy%20Shell%202.png)      
</br>
</br>
8.使用MySQL数据库图形化操作工具Navicat Premium 12对数据库进行操作，图为设计表，添加的字段↓</br>
</br>
![ScreenShot 8](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/8.MySQL%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E8%AE%BE%E8%AE%A1.png)      
</br>
</br>
9.将爬取下来的数据存储的MySQL中，定义的字段所对应的值↓</br>
</br>
![ScreenShot 9](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/9.%E4%BF%9D%E5%AD%98%E5%88%B0MySQL%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD1.png)      
</br>
</br>
10.爬取下来的数据异步保存到MySQL数据库中↓</br>
</br>
![ScreenShot 10](https://github.com/Mocha-Pudding/Scrapy_jianshuSpider/blob/master/images/10.%E4%BF%9D%E5%AD%98%E5%88%B0MySQL%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD2.png)      
</br>

