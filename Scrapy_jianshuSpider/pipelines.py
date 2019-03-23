# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# import pymysql
#
# class ScrapyJianshuspiderPipeline(object):
#     def __init__(self):
#         dbparams = {
#             'host': '127.0.0.1',
#             'port': 3306,
#             'user': 'root',
#             'password': 'password',
#             'database': 'jianshu',
#             'charset': 'utf8'
#         }
#         # **dbparams等价于将定义的关键字参数传递进去
#         # **dbparams会把字典当中的key和value当作关键字参数放到里面来
#         self.conn = pymysql.connect(**dbparams)
#         self.cursor = self.conn.cursor()
#         self._sql = None
#
#     def process_item(self, item, spider):
#         self.cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['article_id'],item['origin_url']))
#         self.conn.commit()
#         return item
#
#     @property
#     def sql(self):
#         if not self._sql:
#             self._sql = """
#             insert into article(id,title,content,author,avatar,pub_time,article_id,origin_url) values(null,%s,%s,%s,%s,%s,%s,%s)
#             """
#             return self._sql
#         return self._sql


#################### 采用twisted异步保存到mysql ####################
# twisted提供的数据库连接的ConnectionPool连接池
# 把插入数据的动作变成异步，从而提高整个爬虫的效率

import pymysql
from twisted.enterprise import adbapi   # 此模块专门用来做数据库处理
from pymysql import cursors

class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'password',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor  # 需要多传递一个参数 游标的类
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id,title,content,author,avatar,pub_time,article_id,origin_url,read_count,like_count,words_count,comment_count,subjects) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
            """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['article_id'],item['origin_url'],item['read_count'],item['like_count'],item['words_count'],item['comment_count'],item['subjects']))

    # 错误处理函数
    def handle_error(self,error,item,spider):
        print('='*10 + "error" + '='*10)
        print(error)
        print('='*10 + "error" + '='*10)