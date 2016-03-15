from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^(?P<page>[0-9]+)?$', views.ArticleListView.as_view(), name = 'index'),
]
