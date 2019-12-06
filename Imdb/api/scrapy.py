import requests
from bs4 import BeautifulSoup
import re

class Scrapy(object):

    def __init__(self, url):
        self.url = url

    def getHtml(self):
        response = requests.get(self.url)
        response.encoding = response.apparent_encoding
        return response

    def getInfo(self, html):
        soup = BeautifulSoup(html, 'lxml')
        movies = soup.select('tbody tr')
        for movie in movies:
            poster = movie.select_one('.posterColumn')
            score = poster.select_one('span[name="ir"]')['data-value']
            movie_link = movie.select_one('.titleColumn').select_one('a')['href']
            year_str = movie.select_one(
                '.titleColumn').select_one('span').get_text()
            year_pattern = re.compile(r'\d{4}')
            year = int(year_pattern.search(year_str).group())
            id_pattern = re.compile(r'(?<=tt)\d+(?=/?)')
            movie_id = int(id_pattern.search(movie_link).group())
            movie_name = movie.select_one('.titleColumn').select_one('a').string
            yield {
                'movie_id': movie_id,
                'movie_name': movie_name,
                'year': year,
                'movie_link': 'https://www.imdb.com' + movie_link,
                'movie_rate': round(float(score), 2),
            }

    def store(self, Models):
        response = self.getHtml().text
        for each in self.getInfo(response):
            Models.objects.update_or_create(name=each['movie_name'], link=each['movie_link'],
                                          year=each['year'], movieId=each['movie_id'],
                                          rate=each['movie_rate'])
