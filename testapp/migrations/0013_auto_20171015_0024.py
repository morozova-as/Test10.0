# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-14 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_auto_20171015_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mas_id_n',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mas_num',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mas_num_last',
        ),
    ]