# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=100)),
                ('channel', models.IntegerField()),
                ('location', models.TextField(max_length=200)),
            ],
        ),
    ]