# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170228_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='job',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
