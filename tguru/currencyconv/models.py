from django.db import models
from django.utils import timezone

class Reviews(models.Model):
    #reviewedobject = models.ForeignKey('blog.Post', related_name='reviewss')
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def post(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Countries(models.Model):
    country_name = models.CharField(max_length=300)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    currency_code = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name
    #the __str__ method is called when you print an instance of the review class

class TransactionFile(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')