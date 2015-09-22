from django.shortcuts import render
from currencyconv.script import CurrencyConverter
import json
import urllib2
from django.http import HttpResponse
# Create your views here.
def convert(request):
    #return HttpResponse("hello")
    if request.method == 'POST':
        yql_base_url = "https://query.yahooapis.com/v1/public/yql"
        yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+request.POST['CurrencyFrom']+request.POST['CurrencyTo']+'")'
        yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        yql_response = urllib2.urlopen(yql_query_url)
        yql_json = json.loads(yql_response.read())
        result = float(request.POST['amount']) * float(yql_json['query']['results']['rate']['Rate'])
        return HttpResponse("%f %s = %f %s" % (float(request.POST['amount']),request.POST['CurrencyFrom'],float(result), request.POST['CurrencyTo']))
    else:
        return render(request, 'currencyconv/currencycalc.html')
    #return render(request, 'landingpage/landing.html')


