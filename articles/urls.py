from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^(?P<page>[0-9]+)?$', views.article_list, name = 'index'),
]
