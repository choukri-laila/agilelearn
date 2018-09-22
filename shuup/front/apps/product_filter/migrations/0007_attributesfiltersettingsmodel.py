# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-14 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0045_disable_default_marketing_permission'),
        ('product_filter', '0006_auto_20180714_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributesFilterSettingsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('filter_type', models.SmallIntegerField(choices=[(1, 'Checkbox'), (2, 'Droupbox'), (3, 'Range')], verbose_name='Filter type')),
                ('attribute', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shuup.Attribute')),
            ],
        ),
    ]
