# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#定义抓取数据结构
class YybItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    apk_type = scrapy.Field() #应用类型
    app_name = scrapy.Field() #应用名字
    star = scrapy.Field()  #应用星级
    apk_Name = scrapy.Field()#包名
    apk_size = scrapy.Field()#apk大小
    download_count = scrapy.Field()#下载次数
    # category = scrapy.Field()
    download_url = scrapy.Field()#下载链接
    app_introduce = scrapy.Field()#应用介绍
    app_icon = scrapy.Field()#应用图标
    app_version = scrapy.Field()#版本号
    update_time = scrapy.Field()#更新时间
    developer = scrapy.Field()#开发商


class AppItem(scrapy.Item):
    app_name = scrapy.Field()
    star = scrapy.Field()