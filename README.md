# Restful-APIs

## 1. Snippets
The snippets api has: id, title, code, language, tyle items in each record. It also supports .json or .api format as its suffix_patterns. The permission here has IsAuthenticatedOrReadOnly, which means only admin can edit online. The feasible queries contain   
[/snippets/](http://fredsnippet.herokuapp.com/snippets/)  
[/sinppets/.json](http://fredsnippet.herokuapp.com/snippets/.json)  
[/snippets/?page=3](http://fredsnippet.herokuapp.com/snippets/?page=3)  
[/snippets/id/](http://fredsnippet.herokuapp.com/snippets/38/)   

## 2. Imdb movies
This api provides access to the top 250 movies in IMDB. Each record consists of id, movieId, movie name, release year, rate, and link to the page of movies. It also supports .json or .api format as its suffix_patterns. The feasible queries contain  
[/movies/](http://fredimdb.herokuapp.com/movies/)  
[/moives/.json](http://fredimdb.herokuapp.com/movies/.json)   
[/movies/?page=3](http://fredimdb.herokuapp.com/movies/?page=3)  
[/movies/detail/movieId/](http://fredimdb.herokuapp.com/movies/detail/17925/)  

## 3. NBA players
The nba players api has: id, playerName, playerNumber, team, height, weight, birthday, age, years in nba, basketball position, link items in each record. It supports .json or .api format as its suffix_patterns. The feasible queries contain  
[/nba/](http://frednba.herokuapp.com/nba/)  
[/nba/.json](http://frednba.herokuapp.com/nba/.json)  
[/nba/?page=3](http://frednba.herokuapp.com/nba/?page=3)  
[/nba/age/24/](http://frednba.herokuapp.com/nba/age/24/)  
[/nba/year_in_nba/3/](http://frednba.herokuapp.com/nba/year_in_nba/3/)  
[/nba/position/Guard/](http://frednba.herokuapp.com/nba/position/Guard/)  
[/nba/team/Utah Jazz/](http://frednba.herokuapp.com/nba/team/Utah%20Jazz/)

## 4. Countries
The countries api has: id, country name, capital of country, populations, area, continent, currency, phone prefix items in each record. It supports .json or .api format as its suffix_patterns. The feasible queries contain  
[/country/](https://fredcountry.herokuapp.com/country/)  
[/country/?format=json](https://fredcountry.herokuapp.com/country/?format=json)  
[/country/?page=3](https://fredcountry.herokuapp.com/country/?page=3)  
[/country/id/](https://fredcountry.herokuapp.com/country/24/)  
[/country/name/](https://fredcountry.herokuapp.com/country/name/Argentina/)  
[/country/capital/](https://fredcountry.herokuapp.com/country/capital/Buenos%20Aires/)  
[/country/currency/](https://fredcountry.herokuapp.com/country/currency/Peso/)  
[/country/continent/](https://fredcountry.herokuapp.com/country/continent/AS/)  
