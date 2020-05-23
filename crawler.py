import requests
import re
starting_url = "https://api.publicapis.org/"

class API_Crawler(object):
    def __init__(self, starting_url):
        self.starting_url = starting_url
        self.visited = set()

    def start(self):
        pass

if __name__ == "__main__":
    crawler = API_Crawler(starting_url)
    crawler.start()