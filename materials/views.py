from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
# from django.urls import reverse
# from django.views import generic
# from django.template import loader
import json

def index(request):
    with open('./materials/contents_api.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for content in data['contents']:
        # print(content['count'], content["next"])
    # contents =contents.object.all()
        return render(request, "materials/home.html", {'data':data})

def about(request):
    return render(request, 'materials/basic.html', {'content':['about me', 'add a link her']})

# def articles(request):
#     with open("./materials/quotes_api.json", 'r', encoding='utf-8') as json_data:
#         data = json.load(json_data)

#     # for quote in data['quotes']:
#     #     print(quote["CompanyName"])
        
#     return render(request, 'articles/articles.html', {'data':data})

# def contentList(request):
#     with open('./materials/contents_api.json', 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file)

#     for content in data['contents']:
#         print(content['count'], content["next"])

    # return HttpResponse("Hello, world. You're at the materials index.")

        # return render(request, "materials/index.html", {'data':data})
# def detail(request, article_id):
#     return HttpResponse("You're looking at article %s." % article_id)

