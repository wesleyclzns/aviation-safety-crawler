import scrapy
from urllib.parse import urljoin


class AnsWikiSpider(scrapy.Spider):
    name = 'answikiano'
    start_urls = ['https://aviation-safety.net/wikibase/']
    
    def parse(self, response):
        #Pega a informação dos acidentes
        
        anos=[]
        anos1 = int(response.css('font+ a ::text').get())
        anos2 = response.css('a+ a ::text').getall()
        anos3 = response.css('br+ a ::text').getall()
        
        
        anos.append(anos1)

        for ano in anos2:
            anos.append(ano)

        for ano in anos3:
            anos.append(ano) 

        urlPrincipal = 'https://aviation-safety.net'
        urlHome = 'https://aviation-safety.net/wikibase'
        urlBaseAno = '/dblist.php?Year='
        urlPagina = '&sorteer=datekey&page='
        urlCasosAno = urljoin(urlHome, urlBaseAno)

        for ano in anos:
            urlAno = (urlCasosAno + str(ano))
            urlAnos.append(urlAno)
            
            for linkAno in urlAnos:
                start_urls = [linkAno]

                casos = response.css('.nobr a ::attr(href)').getall()

                    for caso in casos:
                        urlCaso = (urlPrincipal + str(caso))
                        urlCasos.append(urlCaso)

                        for linkCaso in urlCasos:
                            start_urls = [linkAno]

                            yield{

                                'ano': ano

                                #ID, data e horario
                                'idWiki': response.css('.pagetitle ::text').get(),
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
                                'pais': response.css('img+ a ::text').get(),
                                'coordenadas': response.css('br+ iframe').attrib['src'][53:],
                                'aeroportoOrigem': response.css('tr:nth-child(14) .desc ::text').get(),
                                'aeroportoDestino': response.css('tr:nth-child(15) .desc ::text').get(),
                                'narativa': response.css('br+ span ::text').get(),
                            }



    pass