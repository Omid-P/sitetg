__author__ = 'alexhooker'

import MySQLdb
import grequests
from .models import Provider, Country, Currency

#need to think about how these variables could be defined within my functions (if, that is, they need to be)
def extract_rate(json_res, rate_lookup):
    i = 0
    while i < len(rate_lookup):
        json_res = json_res[rate_lookup[i]]
        i = i+1
    return float(json_res)
    
def hook_wrapper(result_list):
    def add_response(r, *args, **kwargs):
        rjs = r.json()
        rjs['url'] = r.url
        result_list.append(rjs)
    return add_response

def compare_rates(country_from, country_to, amount):
    prov_list = Provider.objects.all().distinct()
    results=[]
    rates = []
    response_methods = {}
    for provider in prov_list:
        if provider.name == 'Xendpay':
            provider.response_item = ['xpRate']
        elif provider.name == 'Azimo':
            provider.response_item = ['rate','rate']
        response_methods[provider.format_url(country_from,country_to,amount)] = {
                    'response_item': provider.response_item, 'name': provider.name}
    
    rs = [grequests.get(provider.format_url(country_from,country_to,amount),
                        hooks={'response': [hook_wrapper(results)]}, timeout=3.501) for provider in prov_list]
    done = grequests.map(rs) #this is required to actually send the requests.
    for json_res in results:
        prov = response_methods[json_res['url']]
        rate_lookup = prov['response_item']
        name = prov['name']
        try:
            rates.append({'name': name, 'rate': extract_rate(json_res, rate_lookup)})
        except:
            rates.append({'name': name, 'rate': 'error'})
    ordered = sorted(rates, key=lambda k: k['rate'], reverse=True)
    return ordered

def currency_converter(currency_from, currency_to, amount):
    import urllib2
    import json
    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
    yql_query = ('select%20*%20from%20yahoo.finance.'
                 'xchange%20where%20pair%20in%20("'+currency_from+currency_to+'")')
    yql_query_url = (yql_base_url + "?q=" +
                     yql_query + "&format=json&env=store%3A%2F%2Fdatatables."
                                 "org%2Falltableswithkeys")
    try:
        yql_response = urllib2.urlopen(yql_query_url)
        try:
            yql_json = json.loads(yql_response.read())
            currency_output = (amount *
                               float(yql_json['query']['results']['rate']['Rate']))
            Error='NULL'
            return currency_output
        except:
            return
    except:
        return

def name(num):
    return num*10000000.0

#def currencylist():
#    r = requests.get('http://openexchangerates.org/currencies.json')
#    currencies = r.json()
#for key in currencies.keys():
#    cur.execute("INSERT INTO currency_list (code, name) VALUES('%s', '%s')" %(key, currencies[key]))



#con = MySQLdb.connect(host="localhost",user="root",passwd="tgpass",db="tguru")
# cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
#INSERT INTO tbl_name (col1,col2) VALUES(15,col1*2);
# cur.execute('select * from currency_list')
# cur.fetchall()
# con.commit()
# con.close()


#import json
#import urllib2
#def CurrencyConverter(currency_from, currency_to, amount):
#    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
#    yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+currency_from+currency_to+'")'
#    yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
#    try:
#        yql_response = urllib2.urlopen(yql_query_url)
#        try:
#            yql_json = json.loads(yql_response.read())
#            currency_output = amount * float(yql_json['query']['results']['rate']['Rate'])
#            Error='NULL'
#            return currency_output
#        except:
#            return
#    except:
#        return