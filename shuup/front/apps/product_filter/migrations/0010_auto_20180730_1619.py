# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_filter', '0009_auto_20180730_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributesfiltersettingsmodel',
            options={'verbose_name': 'Filter attribute setting', 'verbose_name_plural': 'Filter attributes settings'},
        ),
        migrations.AlterModelOptions(
            name='categoriesfiltersettingsmodel',
            options={'verbose_name': 'Filter category setting', 'verbose_name_plural': 'Filter categories settings'},
        ),
        migrations.RemoveField(
            model_name='categoriesfiltersettingsmodel',
            name='filter_type',
        ),
    ]
