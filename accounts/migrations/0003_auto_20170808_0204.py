# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170630_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, upload_to='public/images/%Y/%m/%d'),
        ),
    ]