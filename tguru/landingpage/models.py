from django.db import models

# Create your models here.
class Email(models.Model):
    address = models.CharField(max_length=200)
    signup_date = models.DateTimeField()