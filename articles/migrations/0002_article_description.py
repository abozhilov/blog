# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default=''),
        ),
    ]