# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20170228_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(default='description default text')),
                ('location', models.CharField(default='my location default', max_length=120)),
                ('job', models.CharField(default='my job default', max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
