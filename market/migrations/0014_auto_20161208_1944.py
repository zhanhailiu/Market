# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_auto_20161208_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='nick_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.PositiveIntegerField(blank=True, default='30', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='width',
            field=models.PositiveIntegerField(blank=True, default='30', editable=False, null=True),
        ),
    ]