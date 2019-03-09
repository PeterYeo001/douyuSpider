# -*- coding: utf-8 -*-
#斗鱼热门美女主播图片抓取
import scrapy
import json
from douYu.items import DouyuItem
class SouyuspiderSpider(scrapy.Spider):
    name = 'douyuSpider'
    allowed_domains = ['capi.douyucdn.cn']
    #观察url地址的规律，发现加载下一批主播只有offset的值在变化
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [url + str(offset)]


    def parse(self, response):
        data = json.loads(response.text)["data"]
        for each in data:
            item = DouyuItem()
            item["nickname"] = each["nickname"]
            item["imagelink"] = each["vertical_src"]

            yield item
        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset),callback = self.parse)