# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_announcement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Announcement',
        ),
    ]
