__author__ = 'alexhooker'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.convert)
    ]