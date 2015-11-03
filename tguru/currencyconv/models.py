from django.db import models
from django.utils import timezone



class Currency(models.Model):
     enabled = models.BooleanField(default=True)
     code = models.CharField(max_length=3)
     name = models.CharField(max_length=100)

     def __str__(self):
        return self.code

class Country(models.Model):
    enabled = models.BooleanField(default=True)
    country_name = models.CharField(max_length=300)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    currency = models.ForeignKey(Currency) #many to one - many countries for one currency: Country.currency or Currency.countries_set!

    def __str__(self):
        return self.country_name
    #the __str__ method is called when you print an instance of the review class

class Provider(models.Model):
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    PROVIDER_TYPE_CHOICES = (
        ('FX', 'Foreign exchange'),
        ('TR', 'Travel money'),
        )
    provider_type = models.CharField(max_length=2, choices=PROVIDER_TYPE_CHOICES, default='FX')
    redirect_url = models.CharField(max_length=300)
    scrape_url = models.CharField(max_length=300)
    SCRAPE_TYPE_CHOICES = (
        ('API', 'API'),
        ('BR', 'Emulated Browser'),
            )
    scrape_type = models.CharField(max_length=3, choices=SCRAPE_TYPE_CHOICES, default='API')
    information = models.TextField(blank=True)
    # I think maybe I should just add individual methods to my providers when scraping
    # request_method = models.CharField(max)
    currencies = models.ManyToManyField(Currency) #many to many - a channel is associated with many currencies; a currency is associated with many channels
    def format_url(self, country_from, country_to, amount):
        param_list = []
        lookup = {'country_from.iso2': country_from.iso2, 'country_from.iso3': country_from.iso3,
         'country_from.currency_code': country_from.currency_code, 'country_to.iso2': country_to.iso2,
         'country_to.iso3': country_to.iso3, 'country_to.currency_code': country_to.currency_code, 'amount': amount}
        params = [lookup[i] for i in self.apiparams_set.all()] #this isn't going to work at the moment - I'll get a list of objects.
        return self.url.format(*params)
    def get_rate(self, url):
        if self.request_method == 'get':
            r = requests.get(url)
            return r.json()
    def __str__(self):
        return self.name
class TransactionFile(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Apiparams(models.Model):
    CF2 = 'country_from.iso2'
    CF3 = 'country_from.iso3'
    CFC = 'country_from.currency_code'
    CT2 = 'country_to.iso2'
    CT3 = 'country_to.iso3'
    CTC = 'country_to.currency_code'
    PARAM_CHOICES = (

        (CF2,'country_from.iso2'),
        (CF3, 'country_from.iso3'),
        (CFC, 'country_from.currency_code'),
        (CT2, 'country_to.iso2'),
        (CT3, 'country_to.iso3'),
        (CTC, 'country_to.currency_code'),
        )
    param = models.CharField(max_length = 50, choices=PARAM_CHOICES)
    order_number = models.IntegerField()
    provider = models.ForeignKey(Provider) #many to one - many params for one provider

# class Review(models.Model):
#     #reviewedobject = models.ForeignKey('blog.Post', related_name='reviewss')
#     author = models.CharField(max_length=30)
#     title = models.CharField(max_length=200)
#     rating = models.IntegerField(default=0)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#     provider = models.ForeignKey(Provider)

#     def post(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title

class ExchangeRate(models.Model):
    created_date = models.DateTimeField(
            default=timezone.now)
    rate = models.FloatField()
    yahoo_rate = models.FloatField(null=True)
    provider = models.ForeignKey(Provider)
    to_currency = models.ForeignKey(Currency,related_name='exchange_to')
    from_currency = models.ForeignKey(Currency,related_name='exchange_from')

class Fee(models.Model):
    from_currency = models.ForeignKey(Currency, related_name='fees_to')
    to_currency = models.ForeignKey(Currency, related_name='fees_from')
    provider = models.ForeignKey(Provider)
    fixed_sending_fee = models.DecimalField(max_digits=19,decimal_places=2,null=True)
    fixed_receiving_fee = models.DecimalField(max_digits=19,decimal_places=2,null=True)
    percentage_sending_fee = models.FloatField(null=True)
    percentage_receiving_fee = models.FloatField(null=True)
    minimum_fee = models.DecimalField(max_digits=19,decimal_places=2,null=True)
    threshold = models.DecimalField(max_digits=19,decimal_places=2,null=True)





