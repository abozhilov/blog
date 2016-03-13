from django.contrib import admin
from articles import models

admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(models.Article)
