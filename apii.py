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
print(f"Count : {category_list.get('count')}")
print("Categories : ")
for i in category_list.get('categories'):
    print(i)

