__author__ = 'alexhooker'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.convert),
    url(r'^suggest_currency/$', views.suggest_currency, name='suggest_currency'),
    url(r'^calculate/$', views.ajaxcalc)
    ]