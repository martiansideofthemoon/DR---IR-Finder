# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drirfinder', '0003_auto_20150427_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='department',
            field=models.CharField(default=b'null', max_length=128),
        ),
    ]
