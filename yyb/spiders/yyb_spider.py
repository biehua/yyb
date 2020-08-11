# -*- coding: utf-8 -*-
import scrapy
from yyb.items import YybItem
from yyb.items import AppItem


class YybSpiderSpider(scrapy.Spider):
    #爬虫名
    name = 'yyb_spider'
    #允许的域名，非此域名不会抓取
    allowed_domains = ['sj.qq.com/myapp/']
    #入口url，扔到调度器里---下载器
    start_urls = ['https://sj.qq.com/myapp/category.htm']

#解析包名 生成详细地址yield 回调  解析详细页面信息yield给pip
    def parse(self, response):
        #获取app分类的属性及列表
        appType = response.xpath("//ul[@class='menu-junior']/li")
        for app_type in appType:
            yyb_item = YybItem()
            yyb_item['apk_type'] = app_type.xpath("./a/@href").extract()
            # print(yyb_item)
            #如果属性不为全部软件，生成新的分类url
            if yyb_item['apk_type'][0] != "?orgame=1":
                app_type_url = 'https://sj.qq.com/myapp/category.htm' + yyb_item['apk_type'][0]
                if app_type_url is not None:
                    # print(app_type_url)

                    #yield提交数据到调度器
                    yield scrapy.Request(url=app_type_url, callback=self.parse_type, dont_filter=True)

    #解析
    def parse_type(self, response):
        #打印返回信息
        # print(response.text)
        #获取所有应用列表
        appUrl = response.xpath("//div[@class='main']//ul[@class='app-list clearfix']/li")
        for item_appUrl in appUrl:
            yyb_item = YybItem()
            yyb_item['apk_Name'] = item_appUrl.xpath(".//div[@class='app-info clearfix']/a/@href").extract()
            #获取每个应用的url地址
            detail_url = 'https://sj.qq.com/myapp/' + yyb_item['apk_Name'][0]
            print(detail_url)
            if detail_url is not None:
                #dont_fileter：如果不是allowed_domains，设置执行回调函数；存在url被allowed_domains过滤，设置为true，可不被过滤
                #回调函数request会返回一个reponse，返回在对应的parse
                yield scrapy.Request(url=detail_url, callback=self.parse_detail, dont_filter=True)
    def parse_detail(self, response):
        yyb_item = YybItem()
        yyb_item['app_name'] = response.xpath("//div[@class='det-name-int']/text()").extract()
        yyb_item['star'] = response.xpath("//div[@class='com-blue-star-num']/text()").extract()
        yyb_item['apk_type'] = response.xpath("//a[@class='det-type-link']/text()").extract()
        yyb_item['apk_size'] = response.xpath("//div[@class='det-size']/text()").extract()
        yyb_item['download_count'] = response.xpath("//div[@class='det-ins-num']/text()").extract()
        yyb_item['download_url'] = response.xpath("//div[@class='det-ins-btn-box']//a[@class='det-down-btn']/@data-apkurl").extract()
        yyb_item['app_icon'] = response.xpath("//div[@class='det-icon']/img/@src").extract()
        yyb_item['app_version'] = response.xpath("//div[@class='det-othinfo-data']")[0].xpath("./text()").extract()
        yyb_item['update_time'] = response.xpath("//div[@id='J_ApkPublishTime']/text()").extract()
        yyb_item['developer'] = response.xpath("//div[@class='det-othinfo-data']")[2].xpath("./text()").extract()

        #必须yield 才能接收到数据
        yield yyb_item


