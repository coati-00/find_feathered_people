# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindFeatheredPeopleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class FeatheredPersonAdoptAPetItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    species = scrapy.Field()
    color = scrapy.Field()
    age = scrapy.Field()
    gender = scrapy.Field()
    smallphoto = scrapy.Field()
    largephoto = scrapy.Field()
    infobox = scrapy.Field()

class RescueOrgAdoptAPetItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()
    streetaddr = scrapy.Field()
    city = scrapy.Field()
    town = scrapy.Field()
    state = scrapy.Field()
    rescuezip = scrapy.Field()
