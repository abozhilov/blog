from django.shortcuts import render
from django.http import HttpResponse

def article_list(request, page):
    return render(request, 'articles/list.html')
