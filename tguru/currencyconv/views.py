from django.shortcuts import render
#from currencyconv.script import CurrencyConverter
import json
import urllib2
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import MySQLdb
from reviews.models import Review
from django.utils import timezone
from .script import currency_converter, compare_rates
from django.template import RequestContext
from .forms import DocumentForm
from .models import TransactionFile, Country, Currency
from django.shortcuts import render_to_response

db_connection = MySQLdb.connect(host="localhost",
                                        user="root",passwd="tgpass",db="tguru")


def file_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        newdoc = TransactionFile(docfile = request.FILES['docfile'])
        newdoc.save()
        #form.is_valid() isn't working for some reason
#request.FILES, which is a dictionary containing a key for each FileField (or ImageField, or other FileField subclass) in the form. So the data from the above form would be accessible as request.FILES['file'].

#Note that request.FILES will only contain data if the request method was POST and the <form> that posted the request has the attribute enctype="multipart/form-data". Otherwise, request.FILES will be empty.
            # Redirect to the document list after POST
        return HttpResponse('success')
    else:
        form = DocumentForm() # A empty, unbound form

    # Render list page with the documents and the form
    return render_to_response(
        'currencyconv/upload.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def upload_success(request):
    return HttpResponse('Thanks!')


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

def ajaxcalc(request):
    if request.method == 'GET':
        countryfrom = Country.objects.filter(id=request.GET['countryFrom']).first()
        countryto = Country.objects.filter(id=request.GET['countryTo']).first()
        amount = float(request.GET['amount'])
        currencyfrom = countryfrom.currency.code
        currencyto = countryto.currency.code
        result = currency_converter(currencyfrom,
                                    currencyto, amount)
        compare = compare_rates(countryfrom, countryto, amount)
        return HttpResponse(json.dumps({'res': result, 'comp': compare}), content_type="application/json")

def convert(request):
    #return HttpResponse("hello")
    if request.method == 'POST':
        yql_base_url = "https://query.yahooapis.com/v1/public/yql"
        currencyfrom = Country.objects.filter(id=request.POST['countryFrom']).first().currency.code
        currencyto = Country.objects.filter(id=request.POST['countryTo']).first().currency.code
        yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+currencyfrom+currencyto+'")'
        yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        yql_response = urllib2.urlopen(yql_query_url)
        yql_json = json.loads(yql_response.read())
        result = float(request.POST['amount']) * float(yql_json['query']['results']['rate']['Rate'])
        return HttpResponse("%f %s = %f %s" % (float(request.POST['amount']),request.POST['currencyFrom'],float(result), request.POST['currencyTo']))
    else:
        # currencies, names = get_currencies(db_connection)
        countries = Country.objects.filter(enabled=True).order_by('country_name')
        reviews = Review.objects.all().order_by('published_date')
        return render(request, 'currencyconv/currencycalc.html', {'countries': countries, 'reviews': reviews})
    #return render(request, 'landingpage/landing.html')


def review_handler(request):
    if request.method == 'POST':
        rev = Review(title=request.POST['title'], rating=request.POST['rating'],
                      author=request.POST['revName'], text=request.POST['revText'],
                      created_date=timezone.now())
        rev.post()
        return HttpResponse("Thanks")




# def comparefx(request):
#     if request.method == 'GET':
#         c_from, c_to, amount = (request.GET['currencyFrom'],
#                                     request.GET['currencyTo'], float(request.GET['amount']))
#         xend_url = "https://secure.xendpay.com/startquote/api/quote/"
#         /GB/GBP/FR/EUR

#         "https://secure.xendpay.com/startquote/api/quote/${fromCurrency?.siteSpecificCountryName}/${fromCurrency?.siteSpecificValue}/${toCurrency?.siteSpecificCountryName}/${toCurrency?.siteSpecificValue}/200.00/SR?json"
#         return HttpResponse(json.dumps({'res': result}), content_type="application/json")
