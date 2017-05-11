# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=30)),
                ('confirm', models.CharField(max_length=30)),
            ],
        ),
    ]
