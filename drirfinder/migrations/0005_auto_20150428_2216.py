# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drirfinder', '0004_auto_20150428_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cpi',
            field=models.DecimalField(default=0.0, max_digits=3, decimal_places=2),
        ),
    ]
