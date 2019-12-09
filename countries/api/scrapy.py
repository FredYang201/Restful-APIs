import requests
from lxml import etree
import time
from faker import Faker


class CountryInfo(object):

    def __init__(self, url, page):
        self.url = url
        self.page = page
        self.faker = Faker()

    def getHtml(self, url):
        header = {
            'User-Agent': self.faker.user_agent(),
        }
        response = requests.get(url, headers=header)
        response.encoding = response.apparent_encoding
        return response.text

    def getLink(self, html):
        obj = etree.HTML(html)
        linkReg = '//*[@id="results"]/table/tr/td/div/a/@href'
        links = obj.xpath(linkReg)
        for link in links:
            yield link

    def getInfo(self, html):
        obj = etree.HTML(html)
        baseReg = '//*[@id="places_{}__row"]/td[2]/{}'
        infoDict = {'National flag': ['national_flag', 'img/@src'],
                    'Area': ['area', 'text()'],
                    'Population': ['population', 'text()'],
                    'Country': ['country', 'text()'],
                    'Capital': ['capital', 'text()'],
                    'Continent': ['continent', 'a/text()'],
                    'Currency Code': ['currency_code', 'text()'],
                    'Currency Name': ['currency_name', 'text()'],
                    'Phone': ['phone', 'text()'],
                    }
        result = {
            item: obj.xpath(
                baseReg.format(
                    infoDict[item][0],
                    infoDict[item][1]))[0] for item in infoDict}
        print(result)
        return result

    def store(self, Model):
        for i in range(1, self.page + 1):
            pageUrl = self.url + '/places/default/index/{}'.format(i)
            response = self.getHtml(pageUrl)
            for each in self.getLink(response):
                try:
                    eachUrl = self.url + each
                    time.sleep(5)
                    eachHtml = self.getHtml(eachUrl)
                    result = self.getInfo(eachHtml)
                    Model.objects.get_or_create(
                        name=result['Country'],
                        capital=result['Capital'],
                        population=result['Population'],
                        area=result['Area'],
                        continent=result['Continent'],
                        currency=result['Currency Name'],
                        phone=result['Phone'],
                        flag=self.url + result['National flag'])
                except:
                    pass