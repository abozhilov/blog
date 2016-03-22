from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^(?P<page>[0-9]+)?$', views.ArticleListView.as_view(), name = 'index'),
    url(r'^category/(?P<cat_id>[0-9]+)/(?P<page>[0-9]+)?$', views.CategoryListView.as_view(), name = 'category'),
    url(r'^tag/(?P<tag_id>[0-9]+)/(?P<page>[0-9]+)?$', views.TagListView.as_view(), name = 'tag'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article, name = 'article'),
]
