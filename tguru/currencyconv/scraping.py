import requests
import pandas
import grequests

class Country(object):
	def __init__(self, country_name, countries_df):
		self.country_name = country_name
		self.iso2 = countries_df[countries_df['name']==country_name].iloc[0]['ISO3166-1-Alpha-2']
		self.iso3 = countries_df[countries_df['name']==country_name].iloc[0]['ISO3166-1-Alpha-3']
		self.currency_code = countries_df[countries_df['name']==country_name].iloc[0]['currency_alphabetic_code']

def scrape_rates(from_country, to_country, amount):
	from_country = Country(from_country, countries)
