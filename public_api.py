import requests
URl = "https://api.publicapis.org"
TOKEN_URL = "https://public-apis-api.herokuapp.com/api/v1/auth/token"
URL = "https://public-apis-api.herokuapp.com/api/v1/apis/categories?page=1"
def get_token ():
    url = "https://public-apis-api.herokuapp.com/api/v1/auth/token"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.json())
#data = get_token()
#print(data.get('token'))

def print_json(data):
    print(f"Count : {data.get('count')}")
    print("Categories : ")
    for i in data.get('categories'):
        print(i)

token = f"Bearer {get_token().get('token')}"


def get_list():
    url = "https://public-apis-api.herokuapp.com/api/v1/apis/categories?page=1"
    token = f"Bearer {get_token().get('token')}"
    print(token)
    payload = {}
    headers = {"Authorization": token}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json())
    return response.json()

category_list = get_list()



def category_crawler(category):
    print(f"Crawling {category} : ")
    url = f"https://public-apis-api.herokuapp.com/api/v1/apis/entry?page=2&category={category}"

    payload = {}
    headers = {"Authorization": token}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
    print_json(response.json())
    return response.json()
print_json(category_list)
category_crawler("Animals")

"""category_list_crawling = category_list.get('categories')
for i in category_list_crawling:
    print_json(category_crawler(str(i)))"""