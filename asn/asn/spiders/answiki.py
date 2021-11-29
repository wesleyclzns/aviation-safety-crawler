import scrapy


class AnsWikiSpider(scrapy.Spider):
    name = 'answiki'
    start_urls = ['https://aviation-safety.net/wikibase/269396']

    def parse(self, response):
        #Pega a informação dos acidentes
        yield{
            #ID, data e horario
            'idWiki': response.css('.pagetitle::text').get(),
            'dataOcorencia': response.css('.caption+ .caption ::text').get(),
            'horarioOcorencia': response.css('tr:nth-child(2) .desc ::text').get(),

            #Informações sobre o modelo
            'modelo': response.css('tr:nth-child(3) .desc ::text').get(),
            'modeloLink': response.css('tr:nth-child(3) .desc ::attr(href)').get(),
            'modeloSilueta': response.css('img').attrib['src'],
            'registroAeronave': response.css('tr:nth-child(5) .desc ::text').get(),
            'msn': response.css('tr:nth-child(6) .desc ::text').get(),
            'proprietarioOperador': response.css('tr:nth-child(4) .desc ::text').get(),

            #Informações sobre o incidente
            'fatalidadesOcupantes': response.css('tr:nth-child(7) .desc ::text').get(),
            'outrasFatalidades': response.css('tr:nth-child(8) .desc ::text').get(),
            'danoAeronave': response.css('tr:nth-child(9) .desc ::text').get(),
            'categoriaIncidente': response.css('tr:nth-child(10) .desc ::text').get(),
            'faseVoo': response.css('tr:nth-child(12) .desc ::text').get(),
            'naturezaVoo': response.css('tr:nth-child(13) .desc ::text').get(),

            #Informações sobre a localização do incidente
            'localizacao': response.css('tr:nth-child(11) .desc ::text').get(),
            'coordenadas': response.css('br+ iframe').attrib['src'][53:],
            'aeroportoOrigem': response.css('tr:nth-child(14) .desc ::text').get(),
            'aeroportoDestino': response.css('tr:nth-child(15) .desc ::text').get(),
            'narativa': response.css('br+ span ::text').get(),
        }
        