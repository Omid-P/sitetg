# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20151103_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='provider',
            field=models.ForeignKey(to='currencyconv.Provider', blank=True),
        ),
    ]
