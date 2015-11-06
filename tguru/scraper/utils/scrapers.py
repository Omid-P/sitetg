from currencyconv.models import ExchangeRate, Provider, Country
import requests
from django.utils import timezone

# def scrapers_example(a,b):
# 	return a + b

#write wrapper around functions that return rates to make them save those rates to the database.

def scrape_xendpay():
	countryfrom = Country.objects.filter(iso2='GB').first()
	countryto = Country.objects.filter(iso2='FR').first()
	amount = 200.0
	xend = Provider.objects.filter(name='Xendpay').first()
	url = xend.format_url(countryfrom,countryto,amount)
	r = requests.get(url)
	rate = r.json()['xpRate']
	exchangeRate = ExchangeRate(rate=rate,provider=xend,created_date=timezone.now(),to_currency=countryto.currency,from_currency=countryfrom.currency)
	exchangeRate.save()
	return rate
