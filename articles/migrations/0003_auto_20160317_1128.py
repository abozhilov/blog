# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 11:28
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]