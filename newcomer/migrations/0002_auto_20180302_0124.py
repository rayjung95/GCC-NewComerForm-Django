# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-02 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newcomer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personchurch',
            name='registered_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]