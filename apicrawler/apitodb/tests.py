from django.test import TestCase
from pprint import pprint
#data = {'count': 13, 'categories': [{'API': 'Cat Facts', 'Description': 'Daily cat facts', 'Auth': '', 'HTTPS': True, 'Cors': 'no', 'Link': 'https://alexwohlbruck.github.io/cat-facts/', 'Category': 'Animals'}, {'API': 'Cats', 'Description': 'Pictures of cats from Tumblr', 'Auth': 'apiKey', 'HTTPS': True, 'Cors': 'unknown', 'Link': 'https://docs.thecatapi.com/', 'Category': 'Animals'}, {'API': 'Dogs', 'Description': 'Based on the Stanford Dogs Dataset', 'Auth': '', 'HTTPS': True, 'Cors': 'yes', 'Link': 'https://dog.ceo/dog-api/', 'Category': 'Animals'}, {'API': 'HTTPCat', 'Description': 'Cat for every HTTP Status', 'Auth': '', 'HTTPS': True, 'Cors': 'unknown', 'Link': 'https://http.cat/', 'Category': 'Animals'}, {'API': 'IUCN', 'Description': 'IUCN Red List of Threatened Species', 'Auth': 'apiKey', 'HTTPS': False, 'Cors': 'unknown', 'Link': 'http://apiv3.iucnredlist.org/api/v3/docs', 'Category': 'Animals'}, {'API': 'Movebank', 'Description': 'Movement and Migration data of animals', 'Auth': '', 'HTTPS': True, 'Cors': 'unknown', 'Link': 'https://github.com/movebank/movebank-api-doc', 'Category': 'Animals'}, {'API': 'Petfinder', 'Description': 'Adoption', 'Auth': 'OAuth', 'HTTPS': True, 'Cors': 'yes', 'Link': 'https://www.petfinder.com/developers/v2/docs/', 'Category': 'Animals'}, {'API': 'PlaceGOAT', 'Description': 'Placeholder goat images', 'Auth': '', 'HTTPS': True, 'Cors': 'unknown', 'Link': 'https://placegoat.com/', 'Category': 'Animals'}, {'API': 'RandomCat', 'Description': 'Random pictures of cats', 'Auth': '', 'HTTPS': True, 'Cors': 'yes', 'Link': 'https://aws.random.cat/meow', 'Category': 'Animals'}, {'API': 'RandomDog', 'Description': 'Random pictures of dogs', 'Auth': '', 'HTTPS': True, 'Cors': 'yes', 'Link': 'https://random.dog/woof.json', 'Category': 'Animals'}]}
data = [{'categories': [{'API': 'AniList',
                  'Auth': 'OAuth',
                  'Category': 'Anime',
                  'Cors': 'unknown',
                  'Description': 'Anime discovery & tracking',
                  'HTTPS': True,
                  'Link': 'https://github.com/AniList/ApiV2-GraphQL-Docs'},
                 {'API': 'AnimeNewsNetwork',
                  'Auth': '',
                  'Category': 'Anime',
                  'Cors': 'yes',
                  'Description': 'Anime industry news',
                  'HTTPS': True,
                  'Link': 'https://www.animenewsnetwork.com/encyclopedia/api.php'},
                 {'API': 'Jikan',
                  'Auth': '',
                  'Category': 'Anime',
                  'Cors': 'yes',
                  'Description': 'Unofficial MyAnimeList API',
                  'HTTPS': True,
                  'Link': 'https://jikan.moe'},
                 {'API': 'Kitsu',
                  'Auth': 'OAuth',
                  'Category': 'Anime',
                  'Cors': 'unknown',
                  'Description': 'Anime discovery platform',
                  'HTTPS': True,
                  'Link': 'http://docs.kitsu.apiary.io/'},
                 {'API': 'Studio Ghibli',
                  'Auth': '',
                  'Category': 'Anime',
                  'Cors': 'unknown',
                  'Description': 'Resources from Studio Ghibli films',
                  'HTTPS': True,
                  'Link': 'https://ghibliapi.herokuapp.com'}],
  'count': 5}]


def data_single():
    d = data
    print(d[0].get('categories'))
    ex = d[0].get('categories')
    for i in range(len(ex)):
        pprint(ex[i])

data_single()

def parse_data(data):
    print(len(data))
    count = 0
    pprint(data)
    for i in data:
        count+=10
        print(f"count : {count}")
        i =dict(i)
        keys= i.keys()
        for j in keys:
            print(f"{j} : {i[j]}")
"""    for i in data:
        
        print(f"{i} : {data[i]}")
"""





