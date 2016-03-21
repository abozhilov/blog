from django import template
from django.db.models import Count
from articles.models import Category, Tag

register = template.Library()

@register.inclusion_tag('articles/categories_list.html')
def categories_list():
    return {
        'categories' : Category.objects.all()
    }

@register.inclusion_tag('articles/tags_list.html')
def tags_list():
    return {
        'tags' : Tag.objects.annotate(tag_nums = Count('article')).order_by('-tag_nums')[:5]
    }

