# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-19 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creation', '0002_auto_20190519_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_name',
            new_name='user',
        ),
    ]