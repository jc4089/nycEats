# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 19:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionresults',
            name='inspection_date',
            field=models.DateField(default=datetime.datetime(2017, 1, 10, 19, 29, 19, 243343, tzinfo=utc)),
        ),
    ]
