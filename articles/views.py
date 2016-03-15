from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.models import Category, Tag, Article, Comment

class ArticleView(generic.TemplateView):
    
    def get_context_data(self, **kwrds):
        context = super(ArticleView, self).get_context_data(**kwrds)
        context['categories'] = Category.objects.all()
        
        return context


class ArticleListView(ArticleView):
    template_name = 'articles/list.html'
    
    def get_context_data(self, **kwrds):
        context = super(ArticleListView, self).get_context_data(**kwrds)
        paginator = Paginator(Article.objects.all(), 10)
        page_id = kwrds['page']
        
        try:
            context['articles'] = paginator.page(page_id)
        except PageNotAnInteger:
            context['articles'] = paginator.page(1)
        except EmptyPage:
            context['articles'] = paginator.page(paginator.num_pages)
        
        context['curr_page'] = page_id
        context['last_page'] = paginator.num_pages
        
        return context
    
    


