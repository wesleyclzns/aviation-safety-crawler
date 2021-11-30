import scrapy
from urllib.parse import urljoin


class AnsWikiSpider(scrapy.Spider):
    name = 'answikiano'
    start_urls = ['https://aviation-safety.net/wikibase/']
    
    def parse(self, response):
        
        #Pega os anos 
        anos=[]
        anos1 = int(response.css('font+ a ::text').get())
        anos2 = response.css('a+ a ::text').getall()
        anos3 = response.css('br+ a ::text').getall()
        
        #Coloca em uma lista
        anos.append(anos1)

        for ano in anos2:
            anos.append(ano)

        for ano in anos3:
            anos.append(ano) 

        urlPrincipal = 'https://aviation-safety.net'
        urlHome = urlPrincipal + '/wikibase'
        urlBaseAno = 'dblist.php?Year='
        urlPagina = '&sorteer=datekey&page='
        urlCasosAno = urlHome + urlBaseAno

        #listas de link dos anos
        urlAnos = []
        #lista de link dos casos
        urlCasos = []


        #Pega o numero do ano e coloca no link "https://aviation-safety.net/wikibase/dblist.php?Year=" e faz uma lista
        for ano in anos:
            urlAno = response.url + urlBaseAno + str(ano)
            urlAnos.append(urlAno)

            #Entra em cada um dos link da lista de url dos anos 
            for linkAno in urlAnos:
                scrapy.Request(linkAno)
                
                #Pega o link de cada caso/incidente
                casos = response.css('.nobr a ::attr(href)').getall()

                    for caso in casos:
                        urlCaso = (urlPrincipal + str(caso))
                        urlCasos.append(urlCaso)

                paginas= response.css('.pagenumbers a ::attr(href)').getall()

                    for pagina in paginas:
                        pagina = pagina[10:-1]
                        

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