# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-16 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20190417_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='DOB',
            field=models.DateField(),
        ),
    ]
