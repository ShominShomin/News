# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
