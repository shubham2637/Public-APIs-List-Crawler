from django.shortcuts import render,HttpResponse
from .models import api_detail
from django.forms import modelform_factory
from math import ceil
from pprint import pprint
import requests
# Create your views here.

TOKEN_URL = "https://public-apis-api.herokuapp.com/api/v1/auth/token"

class APIcrawler():
    token = ""
    def __init__(self):
        response = requests.request("GET", TOKEN_URL)
        self.token = f"Bearer {response.json().get('token')}"


    def category_pagewise_crawler(self,category, page_number):
        print(page_number)
        print(f"Crawling {category} Page {page_number} : ")
        url = f"https://public-apis-api.herokuapp.com/api/v1/apis/entry?page={page_number}&category={category}"

        headers = {"Authorization": self.token}

        response = requests.request("GET", url, headers=headers)
        return response.json()

    def page_count(self,data):
        count = data.get('count')
        #print (ceil(count/10))
        return ceil(count / 10)

    def get_all_data_categorywise(self,category):
        datac = []
        pagecount = self.page_count(self.category_pagewise_crawler(category, 1))
        for i in range(1, pagecount + 1):
            datac.append(self.category_pagewise_crawler(category, i))
        return datac


def index(request):
    context = {
    }
    return render(request, "apitodb/index.html", context)

def add(request,category):
    api = APIcrawler()
    data = api.get_all_data_categorywise(category=category)
    ex = data[0].get('categories')
    for i in range(len(ex)):
        pprint(ex[i])
    #for apidetails in data:
        #API = api_detail(apidetails.get('categories'))
        #API.save()

    return HttpResponse(f"{category} Added to Database")


def page_wise_view(request,pnum):
    context = {
    }
    return render(request, "apitodb/page_wise_view.html", context)


