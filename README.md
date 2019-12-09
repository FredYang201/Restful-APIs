# Restful-APIs

## Snippets
The snippets api has: id, title, code, language, tyle items in each record. It also supports .json or .api format as its suffix_patterns. The permission here has IsAuthenticatedOrReadOnly, which means only admin can edit online. The feasible queries contain   
[/snippets/](http://fredsnippet.herokuapp.com/snippets/)  
[/sinppets/.json](http://fredsnippet.herokuapp.com/snippets/.json)  
[/snippets/?page=3](http://fredsnippet.herokuapp.com/snippets/?page=3)  
[/snippets/id/](http://fredsnippet.herokuapp.com/snippets/38/)   

## Imdb movies
This api provides access to the top 250 movies in IMDB. Each record consists of id, movieId, movie name, release year, rate, and link to the page of movies. It also supports .json or .api format as its suffix_patterns. The feasible queries contain /movies/, /moives/.json, /movies/?page=3, /movies/detail/movieId/ and so on.
