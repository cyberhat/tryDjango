# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170228_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='location',
            field=models.CharField(blank=True, default='my location default', max_length=120, null=True),
        ),
    ]
