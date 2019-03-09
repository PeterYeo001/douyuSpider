 # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class DouyuPipeline(object):
 #   def process_item(self, item, spider):
  #      return item
import scrapy,os
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
class ImagesPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings() .get("IMAGES_STORE")
    def get_media_requests(self,item,info):
        image_url = item["imagelink"]
        yield scrapy.Request(image_url, dont_filter=True)

    def item_completed(self,result,item,info):
        image_path = [x["path"] for ok,x in result if ok]
        os.rename(self.IMAGES_STORE + "/" +image_path[0], \
                  self.IMAGES_STORE + "/" + item["nickname"] +'.jpg')

        item["imagesPath"] = self.IMAGES_STORE + "/" + item["nickname"]
        return item