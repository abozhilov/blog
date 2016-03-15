from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.models import Category, Tag, Article, Comment

class BaseArticleView(generic.TemplateView):
    
    def get_context_data(self, **kwrds):
        context = super(BaseArticleView, self).get_context_data(**kwrds)
        context['categories'] = Category.objects.all()
        
        return context


class ArticleListView(BaseArticleView):
    template_name = 'articles/list.html'
    
    def get_context_data(self, **kwrds):
        context = super(ArticleListView, self).get_context_data(**kwrds)
        paginator = Paginator(self.get_paginator_data(), 10)
        page = self.get_page(int(kwrds['page']), paginator.num_pages)
        
        context['articles']  = paginator.page(page)
        context['curr_page'] = page
        context['last_page'] = paginator.num_pages
        
        return context
        
    def get_paginator_data(self):
        return Article.objects.all()
    
    def get_page(self, page, max_page):
        if page is None:
            return 1
        elif page > max_page:
            return max_page
        else:
            return page
    
    


