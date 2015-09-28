__author__ = 'alexhooker'
import requests
import MySQLdb
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