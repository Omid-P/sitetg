from django.shortcuts import render
#from currencyconv.script import CurrencyConverter
import json
import urllib2
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import MySQLdb
from .models import Reviews

db_connection = MySQLdb.connect(host="localhost",user="root",passwd="tgpass",db="tguru")

def get_currencies(db_connection):
    cursor = db_connection.cursor()
    cursor.execute('select * from currency_list order by name;')
    currencylist = cursor.fetchall()
    names = []
    for keyvaluetuple in currencylist:
        names.append(keyvaluetuple[0])
    return currencylist, names

def suggest_currency(request):
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
        currencies, names = get_currencies(db_connection)
        testlist = {'Abc': 'Abcd', 'Abcde': 'Abcdef'}
        res = [k for k in names if starts_with in k]
        #res = ['Allo']
        #return HttpResponse(res)
        return JsonResponse(testlist)

def currencyconverter(currency_from, currency_to, amount):
    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
    yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+currency_from+currency_to+'")'
    yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    try:
        yql_response = urllib2.urlopen(yql_query_url)
        try:
            yql_json = json.loads(yql_response.read())
            currency_output = amount * float(yql_json['query']['results']['rate']['Rate'])
            Error='NULL'
            return currency_output
        except:
            return
    except:
        return


def ajaxcalc(request):
    if request.method == 'GET':
        yql_base_url = "https://query.yahooapis.com/v1/public/yql"
        yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+request.GET['currencyFrom']+request.GET['currencyTo']+'")'
        yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        yql_response = urllib2.urlopen(yql_query_url)
        yql_json = json.loads(yql_response.read())
        result = float(request.GET['amount']) * float(yql_json['query']['results']['rate']['Rate'])
       # return HttpResponse("%f %s = %f %s" % (float(request.POST['amount']),request.POST['currencyFrom'],float(result), request.POST['currencyTo']))
        return HttpResponse(json.dumps({'res': result}), content_type="application/json")


def convert(request):
    #return HttpResponse("hello")
    if request.method == 'POST':
        yql_base_url = "https://query.yahooapis.com/v1/public/yql"
        yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+request.POST['currencyFrom']+request.POST['currencyTo']+'")'
        yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        yql_response = urllib2.urlopen(yql_query_url)
        yql_json = json.loads(yql_response.read())
        result = float(request.POST['amount']) * float(yql_json['query']['results']['rate']['Rate'])
        return HttpResponse("%f %s = %f %s" % (float(request.POST['amount']),request.POST['currencyFrom'],float(result), request.POST['currencyTo']))
    else:
        currencies, names = get_currencies(db_connection)
        reviews = Reviews.objects.all().order_by('published_date')
        return render(request, 'currencyconv/currencycalc.html', {'currencies': currencies, 'reviews': reviews})
    #return render(request, 'landingpage/landing.html')


