# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sku',
            name='sku_five_picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='sku',
            name='sku_four_picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='sku',
            name='sku_one_picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='sku',
            name='sku_six_picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='sku',
            name='sku_three_picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='sku',
            name='sku_two_picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
