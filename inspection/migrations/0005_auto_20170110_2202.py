# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0004_auto_20170110_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionresults',
            name='grade',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(default='American', max_length=100),
        ),
    ]