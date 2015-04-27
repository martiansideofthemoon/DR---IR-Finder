# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drirfinder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='cpi',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=2),
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.CharField(default=b'null', unique=True, max_length=128),
        ),
        migrations.AddField(
            model_name='category',
            name='roll_number',
            field=models.CharField(default=b'0', unique=True, max_length=128),
        ),
    ]
