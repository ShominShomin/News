# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 06:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_war'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='war',
            name='author',
        ),
        migrations.DeleteModel(
            name='War',
        ),
    ]