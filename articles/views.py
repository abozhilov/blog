from django.shortcuts import render
from django.http import HttpResponse

def article_list(request, page):
    print(page)
    return HttpResponse('It works')
