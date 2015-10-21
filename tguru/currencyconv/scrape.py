import requests
import pandas
import time
import grequests

class Country(object):
	def __init__(self, country_name, countries_df):
		self.country_name = country_name
		self.iso2 = countries_df[countries_df['name']==country_name].iloc[0]['ISO3166-1-Alpha-2']
		self.iso3 = countries_df[countries_df['name']==country_name].iloc[0]['ISO3166-1-Alpha-3']
		self.currency_code = countries_df[countries_df['name']==country_name].iloc[0]['currency_alphabetic_code']

countries = pandas.read_csv('country-codes.csv')
print "Enter from country",
from_country = raw_input()
while countries[countries['name']==from_country].empty:
	print "Try again",
	from_country = raw_input()
	# e.g. United Kingdom

from_country = Country(from_country, countries)


print "Enter to country",
to_country = raw_input()
while countries[countries['name']==to_country].empty:
	print "Try again",
	to_country = raw_input()

to_country = Country(to_country, countries)

print "Enter send amount",
send_amount = float(raw_input())
amount = "{0:.2f}".format(send_amount)
print "Send amount = {}".format(amount)



class FXProvider(object):
	def __init__(self, name):
		self.name = name
		self.url = ""
		# e.g. https://secure.xendpay.com/startquote/api/quote/{}/{}/{}/{}/200.00/SR?json
		self.param_list = []
		# e.g. ['country_from.iso2', 'country_from.currency_code', 'country_to.iso2', 'country_to.currency_code']
		self.request_method = ""
		self.response_item = None
		self.type = ""
	def format_url(self, country_from, country_to, amount):
		lookup = {'country_from.iso2': country_from.iso2, 'country_from.iso3': country_from.iso3,
		 'country_from.currency_code': country_from.currency_code, 'country_to.iso2': country_to.iso2,
		 'country_to.iso3': country_to.iso3, 'country_to.currency_code': country_to.currency_code, 'amount': amount}
		params = [lookup[i] for i in self.param_list]
		return self.url.format(*params)
	def get_rate(self, url):
		if self.request_method == 'get':
			r = requests.get(url)
			return r.json()

#			return r.json()[self.response_item]

#rate = r.json(self.response_item)
			



xend = FXProvider('Xendpay')
xend.url = "https://secure.xendpay.com/startquote/api/quote/{}/{}/{}/{}/200.00/SR?json"
xend.param_list = ['country_from.iso2', 'country_from.currency_code', 'country_to.iso2', 'country_to.currency_code']
xend.request_method = "get"
xend.response_item = ['xpRate']
#xend.response_item = 'receive'
# centtrip = FXProvider('Centtrip')
# centtrip.url = "https://www.centtrip.com/getRates.php?c1={}&c2={}"
# centtrip.param_list = ['country_from.currency_code', 'country_to.currency_code']
# centtrip.request_method = "get"

tgo = FXProvider('Transfergo')
tgo.url = 'https://my.transfergo.com//en/user/ajax/booking/convertCurrency?from={}%3A{}&to={}%3A{}&send_amount={}&coupon=&business='
tgo.param_list = ['country_from.iso2', 'country_from.currency_code', 'country_to.iso2', 'country_to.currency_code', 'amount']
tgo.request_method = "get"
#tgo.response_item = 'receive_amount'
tgo.response_item = ['rate']

orb = FXProvider('OrbitRemit')
orb.url = "https://secure.orbitremit.com/api/rates/{}:{}.json"
orb.param_list = ['country_from.currency_code', 'country_to.currency_code']
orb.request_method = "get"
orb.response_item = ["exchangeRate",'Rate','exchangeRate']

azimo = FXProvider('Azimo')
azimo.url = "https://azimo.com/en/rest/countries/{}/rate?payoutCountryIso3Code={}&payoutCurrencyIso3Code={}"
azimo.param_list =['country_from.iso3', 'country_to.iso3', 'country_to.currency_code']
azimo.request_method = "get"
azimo.response_item = ['rate','rate']

prov_list = [xend, tgo, orb, azimo]
response_methods = {}
for provider in prov_list:
	response_methods[provider.format_url(from_country,to_country,amount)] = {'response_item': provider.response_item, 'name': provider.name}
#print response_methods

#ordered = sorted(results, key=lambda k: k['rate'], reverse=True)
#formatted_urls = [provider.format_url(from_country, to_country, amount) for provider in prov_list]

#def print_url(args):
#    print args['url']
results = []

def print_response(r, *args, **kwargs):
	rjs = r.json()
	rjs['url'] = r.url
	results.append(rjs)

rs = [grequests.get(provider.format_url(from_country,to_country,amount),hooks={'response': [print_response]}, timeout=3.501) for provider in prov_list]

#requests.get('http://httpbin.org', hooks=dict(response=print_url))


#requests.get('http://httpbin.org', hooks=dict(response=print_url))
#def print_url(r, *args, **kwargs):
#    print(r.url)
#results = []
t0 = time.time()
#results =[result.json() for result in grequests.map(rs)]
#results = grequests.map(rs)
#for provider in prov_list:
#	results.append({'name': provider.name, 'rate': provider.get_rate(provider.format_url(from_country, to_country, amount))})
#ordered = sorted(results, key=lambda k: k['rate'], reverse=True)
#print ordered
done = grequests.map(rs)
t1 = time.time()
#print results
print t1-t0


rates = []

def extract_rate(json_res):
	i = 0
	while i < len(rate_lookup):
		json_res = json_res[rate_lookup[i]]
		i = i+1
	return float(json_res)

for json_res in results:
	prov = response_methods[json_res['url']]
	rate_lookup = prov['response_item']
	name = prov['name']
	rates.append({'name': name, 'rate': extract_rate(json_res)})

ordered = sorted(rates, key=lambda k: k['rate'], reverse=True)
#print ordered
print ordered
#pass this list to the template

