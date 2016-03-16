from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Count
from django.core.paginator import Paginator
from articles.models import Category, Tag, Article, Comment

class BaseArticleView(generic.TemplateView):
    
    def get_context_data(self, **kwrds):
        context = super(BaseArticleView, self).get_context_data(**kwrds)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.annotate(tag_nums = Count('article')).order_by('-tag_nums')[:5]
        
        return context


class ArticleListView(BaseArticleView):
    template_name = 'articles/list.html'
    
    def get_context_data(self, **kwrds):
        context = super(ArticleListView, self).get_context_data(**kwrds)
        paginator = Paginator(self.get_paginator_data(context, **kwrds), 10)
        page = self.get_page(kwrds['page'], paginator.num_pages)
        
        context['articles']  = paginator.page(page)
        context['curr_page'] = page
        context['last_page'] = paginator.num_pages
        
        return context
        
    def get_paginator_data(self, context, **kwrds):
        return Article.objects.order_by('-publish_date').exclude(draft = True)
    
    def get_page(self, page, max_page):
        if page is None:
            return 1
            
        page = int(page)
        if page > max_page:
            return max_page
        else:
            return page
    

class CategoryListView(ArticleListView):
    
    def get_paginator_data(self, context, **kwrds):
        category = get_object_or_404(Category, pk = kwrds['cat_id'])
        context['title'] = category.name
        
        return category.article_set.order_by('-publish_date').exclude(draft = True)
    
    
class TagListView(ArticleListView):
    
    def get_paginator_data(self, context, **kwrds):
        tag = get_object_or_404(Tag, pk = kwrds['tag_id'])
        context['title'] = tag.name
        
        return tag.article_set.order_by('-publish_date').exclude(draft = True)


class ArticleView(BaseArticleView):
    template_name = 'articles/article.html'
    
    def get_context_data(self, **kwrds):
        context = super(ArticleView, self).get_context_data(**kwrds)
        context['article'] = get_object_or_404(Article, pk = kwrds['article_id'])
        
        return context
