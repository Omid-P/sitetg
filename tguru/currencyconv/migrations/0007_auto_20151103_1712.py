# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencyconv', '0006_auto_20151103_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='provider_type',
            field=models.CharField(default=b'FX', max_length=2, choices=[(b'FX', b'Foreign exchange'), (b'TR', b'Travel money')]),
        ),
    ]
