# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-10 01:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('terreno', '0004_auto_20181104_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='poligono',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
