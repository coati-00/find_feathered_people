import scrapy

class AdoptAPetSpider(scrapy.Spider):
    '''Scraper for getting birds from adopts a pet site'''
    name = "adopt-a-pet"

    def start_requests(self):
        '''initiate scraping'''
        urls = ["http://www.adoptapet.com/pet-adoption/search/bird/100/miles/10016"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''for now save the pages - handle download for each of the
        requests made'''
        initialelement = response.css("div.pet_results.rounded_corner")
        name = initialelement.css('p a.name::text').extract()
        print name
        detailslink = initialelement.css('a::attr(href)').extract()
        print detailslink
        '''species = scrapy.Field()
        color = scrapy.Field()
        age = scrapy.Field()
        gender = scrapy.Field()
        page = response.url.split("/")
        filename = 'petfinder-s%.html' % page
        with open(filename, 'wb') as fil:
            fil.write(response.body)
        self.log('Saved file as %s' % filename)'''
