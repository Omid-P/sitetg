# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencyconv', '0007_auto_20151103_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='currency_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='currency_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='currency_code',
        ),
        migrations.RemoveField(
            model_name='country',
            name='currency_name',
        ),
    ]
