# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=models.TextField(),
        ),
    ]
