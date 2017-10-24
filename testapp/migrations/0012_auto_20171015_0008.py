# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-14 21:08
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mas_id_n',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=0, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mas_num',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=datetime.datetime(2017, 10, 15, 0, 8, 22, 3083), size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mas_num_last',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=0, size=None),
            preserve_default=False,
        ),
    ]