# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 12:08
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20160218_0812'),
    ]

    operations = [
        HStoreExtension()
    ]