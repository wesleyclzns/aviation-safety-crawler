import scrapy


class AnsWikiSpider(scrapy.Spider):
    name = 'answikiano'
    start_urls = ['https://aviation-safety.net/wikibase/']
    
    def parse(self, response):
        #Pega a informação dos acidentes
        
        ano1 = int(response.css('font+ a ::text').get())
        anos2 = response.css('a+ a ::text').getall()
        anos3 = response.css('br+ a ::text').getall()
        
        
        anos.append(ano1)

        for ano in ano2:
            anos.append(ano)

        for ano in ano3:
            anos.append(ano) 

    pass

        


for ano in anos:
    'aviation-safety.net/wikibase/dblist.php?Year=' + ano



             