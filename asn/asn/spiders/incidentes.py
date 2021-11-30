""" import scrapy


class IncidentesSpider(scrapy.Spider):
    name = 'incidentes'
    start_urls = ['https://aviation-safety.net/wikibase/dblist.php?Year=']

    def parse(self, response):
        
        #start_urls + '&sorteer=datekey&page=' + 

       
        caso = []
        casos = response.css('.nobr a ::attr(href)').getall()
        
        casos.append(response.css('.nobr a ::attr(href)').getall())

        pass

 """
