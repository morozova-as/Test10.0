# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-15 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0015_auto_20171015_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
