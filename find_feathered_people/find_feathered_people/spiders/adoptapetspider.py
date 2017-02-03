import scrapy

class AdoptAPetSpider(scrapy.Spider):
    '''Scraper for getting birds from adopts a pet site'''
    name = "adopt-a-pet"

    def start_requests(self):
        '''initiate scraping'''
        urls = ["http://www.adoptapet.com/pet-adoption/search/bird/100/miles/10016"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_details(self, response):
        '''follow link to details page and get detailed info there'''
        details = {'species': '', 'color': '', 'age': '', 'gender': ''}
        rescue = {'name': '', 'phone': '', 'email': '', 'website': '', 'address': ''}
        birdstory = ""
        largephoto = ""
        for element in response.css('div.container div.row'):
            birdinfobox = element.css("div.blue_highlight.no_margin.top_margin_xlarge ul li")
            for each in birdinfobox:
                if each.css("b::text").extract() == [u'Breed']:
                    details['species'] = each.css("li::text").extract()
                if each.css("b::text").extract() == [u'Color:']:
                    details['color'] = each.css("li::text").extract()
                if each.css("b::text").extract() == [u'Age:']:
                    details['color'] = each.css("li::text").extract()
                if each.css("b::text").extract() == [u'Sex:']:
                    details['gender'] = each.css("li::text").extract()
        birdinfostory = response.css("div.info_box.row div div div.body").extract()
        if birdinfostory is not None:
            birdstory = birdinfostory
        birdlargephoto = response.css("div.col-sm-7 div.large_image img::attr(src)").extract()
        if birdlargephoto is not None:
            largephoto = birdlargephoto

        # Also get rescue org info
        rescuesidebar = response.css("div.body.contact_sidebar.hidden-xs")

        # Go over each of the listed items in the side bar and extract correct info
        for each in rescuesidebar.css("ul li"):
            if each.css("b::text").extract() == [u'Rescue Group:']:
                rescue['name'] = each.css("a::text").extract()
            if each.css("b::text").extract() == [u'Phone:']:
                rescue['phone'] = each.css("a::text").extract()
            if each.css("b::text").extract() == [u'E-mail:']:
                rescue['email'] = each.css("a::text").extract()
            if each.css("b::text").extract() == [u'Website:']:
                rescue['website'] = each.css("a::text").extract()
            if each.css("b::text").extract() == [u'Address:']:
                rescue['address'] = each.css("li::text").extract()

        yield {
            'rescue' : rescue,
            'largephoto' : largephoto,
            'birdstory': birdstory,
            'species' : details['species'],
            'color': details['color'],
            'age': details['color'],
            'gender': details['gender'],
        }



    def parse(self, response):
        '''for now save the pages - handle download for each of the
        requests made'''
        # the selector for bird gender seems to return gender
        # and age if there is an age
        for initialelement in response.css("div.pet_results.rounded_corner"):
            detailslink = initialelement.css('a::attr(href)').extract_first()
            if detailslink is not None:
                next_page = response.urljoin(detailslink)
                print "next_page"
                yield scrapy.Request(next_page, callback=self.get_details)
            yield {
                'name' : initialelement.css('p a.name::text').extract(),
                'detailslink' : initialelement.css('a::attr(href)').extract_first(),
                'birdgender' : initialelement.css(
                    "div.pet_results.rounded_corner > a::text").extract(),
                'rescueorgtownstate' : initialelement.css(
                    "p a.smaller_line_height.track::text").extract(),
                'photo' : initialelement.css("img::attr(src)").extract(),
            }
            # name = initialelement.css('p a.name::text').extract()
            # detailslink = initialelement.css('a::attr(href)').extract()
            # # add follow link method
            # birdgender = initialelement.css(":first-child a").extract()
            # rescueorgtownstate = initialelement.css("p a.name").extract()
            # phototag = initialelement.css("span.featured-thumbnail a img").extract()
            # photo = initialelement.css("img::attr(src)").extract()
            # print(dict(name=name, detailslink=detailslink,
            #            birdgender=birdgender,
            #            rescueorgtownstate=rescueorgtownstate,
            #            phototag=phototag, photo=photo))
        # species = scrapy.Field()
        # color = response.css(
        # age = response.css(
        # gender = response.css(
        '''page = response.url.split("/")
        filename = 'petfinder-s%.html' % page
        with open(filename, 'wb') as fil:
            fil.write(response.body)
        self.log('Saved file as %s' % filename)'''
