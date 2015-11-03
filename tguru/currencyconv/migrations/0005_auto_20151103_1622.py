# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('currencyconv', '0004_transactionfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apiparams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('param', models.CharField(max_length=50, choices=[(b'country_from.iso2', b'country_from.iso2'), (b'country_from.iso3', b'country_from.iso3'), (b'country_from.currency_code', b'country_from.currency_code'), (b'country_to.iso2', b'country_to.iso2'), (b'country_to.iso3', b'country_to.iso3'), (b'country_to.currency_code', b'country_to.currency_code')])),
                ('order_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(max_length=300)),
                ('iso2', models.CharField(max_length=2)),
                ('iso3', models.CharField(max_length=3)),
                ('currency_code', models.CharField(max_length=3)),
                ('currency_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency_code', models.CharField(max_length=3)),
                ('currency_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('rate', models.FloatField()),
                ('yahoo_rate', models.FloatField(null=True)),
                ('from_currency', models.ForeignKey(related_name='exchange_from', to='currencyconv.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fixed_sending_fee', models.DecimalField(null=True, max_digits=19, decimal_places=2)),
                ('fixed_receiving_fee', models.DecimalField(null=True, max_digits=19, decimal_places=2)),
                ('percentage_sending_fee', models.FloatField(null=True)),
                ('percentage_receiving_fee', models.FloatField(null=True)),
                ('minimum_fee', models.DecimalField(null=True, max_digits=19, decimal_places=2)),
                ('threshold', models.DecimalField(null=True, max_digits=19, decimal_places=2)),
                ('from_currency', models.ForeignKey(related_name='fees_to', to='currencyconv.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('redirect_url', models.CharField(max_length=300)),
                ('scrape_url', models.CharField(max_length=300)),
                ('scrape_type', models.CharField(default=b'API', max_length=3, choices=[(b'API', b'API'), (b'BR', b'Emulated Browser')])),
                ('information', models.TextField(blank=True)),
                ('currencies', models.ManyToManyField(to='currencyconv.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('provider', models.ForeignKey(to='currencyconv.Provider')),
            ],
        ),
        migrations.DeleteModel(
            name='Countries',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.AddField(
            model_name='fee',
            name='provider',
            field=models.ForeignKey(to='currencyconv.Provider'),
        ),
        migrations.AddField(
            model_name='fee',
            name='to_currency',
            field=models.ForeignKey(related_name='fees_from', to='currencyconv.Currency'),
        ),
        migrations.AddField(
            model_name='exchangerate',
            name='provider',
            field=models.ForeignKey(to='currencyconv.Provider'),
        ),
        migrations.AddField(
            model_name='exchangerate',
            name='to_currency',
            field=models.ForeignKey(related_name='exchange_to', to='currencyconv.Currency'),
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ForeignKey(to='currencyconv.Currency'),
        ),
        migrations.AddField(
            model_name='apiparams',
            name='provider',
            field=models.ForeignKey(to='currencyconv.Provider'),
        ),
    ]
