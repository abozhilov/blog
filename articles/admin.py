from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from articles.models import Author, Category, Tag, Comment, Article

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget' : TinyMCE(attrs={'cols': 120, 'rows': 30})}
    }

admin.site.register(Article, ArticleAdmin)
