# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0002_auto_20161205_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='channel',
            field=models.IntegerField(),
        ),
    ]
