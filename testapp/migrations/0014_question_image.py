# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-14 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_auto_20171015_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/testapp/images/'),
        ),
    ]