# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencyconv', '0003_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
        ),
    ]
