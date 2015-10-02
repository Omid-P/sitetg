
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('landingpage.urls')),
    url(r'^currency/', include('currencyconv.urls')),
    url(r'^tools/', views.toolindex)
]


