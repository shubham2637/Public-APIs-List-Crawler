from math import ceil
import pprint
import requests
URl = "https://api.publicapis.org"
TOKEN_URL = "https://public-apis-api.herokuapp.com/api/v1/auth/token"
URL = "https://public-apis-api.herokuapp.com/api/v1/apis/categories?page=1"
#CATEGORY_LIST = set()




def get_token ():
    response = requests.request("GET", TOKEN_URL)
    return(response.json())

#data = get_token()
#print(data.get('token'))


def print_json(data):
    print(f"Count : {data.get('count')}")
    print("Categories : ")
    for i in data.get('categories'):
        print(i)


token = f"Bearer {get_token().get('token')}"

def get_catorgylist(page_number):
    url = f"https://public-apis-api.herokuapp.com/api/v1/apis/categories?page={page_number}"
    headers = {"Authorization": token}

    response = requests.request("GET", url, headers=headers)

    #print(response.json())
    return response.json()

def get_list_category(category):
    url = f"https://public-apis-api.herokuapp.com/api/v1/apis/entry?page=1&category={category}"
    payload = {}
    headers = {"Authorization": token}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json())
    #return response.json()

def parse_data(Data):
    d =Data.get('categories')
    #print(type(d))
    for i in d:
        print(i)
"""def get_all_list():
    pagecount = 5
    for i in range(1,pagecount+1):
        CATEGORY_LIST.add(get_catorgylist(i).get('categories'))
        pprint.pprint(CATEGORY_LIST)
    print("OK!")
get_all_list()
"""
def page_count(data):
    count = data.get('count')
    #print (ceil(count/10))
    return ceil(count / 10)


def category_pagewise_crawler(category, page_number):
    #print(page_number)
    #print(f"Crawling {category} Page {page_number} : ")
    url = f"https://public-apis-api.herokuapp.com/api/v1/apis/entry?page={page_number}&category={category}"

    headers = {"Authorization": token}

    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()

"""
#print_json(category_list)
Category = get_list_category("Animals")
pagecount = page_count(Category)
print(pagecount)"""

def get_all_data_categorywise(category):
    datac = category_pagewise_crawler(category,1)
    parse_data(datac)
    pagecount = page_count(datac)
    for i in range(2,pagecount+1):
        category_pagewise_crawler(category,i)

CATEGORY_LIST = ['Animals']
for i in CATEGORY_LIST:
    data = get_all_data_categorywise(i)
    print(type(data))





#get_all_data_categorywise("Animals")
#data = category_pagewise_crawler("Animals",2)
#parse_data(data)
"""category_list_crawling = category_list.get('categories')
for i in category_list_crawling:
    print_json(category_crawler(str(i)))"""