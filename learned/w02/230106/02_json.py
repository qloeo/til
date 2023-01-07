import json
from pprint import pprint
with open('data/movie.json', 'r', encoding ='UTF8') as f:
    movie = json.load(f)
    pprint(movie)
    print(type(movie))
    print(movie['title'])