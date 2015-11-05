__author__ = 'alexhooker'
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = patterns('',
#     (r'^', include('myapp.urls')),
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
    url(r'^$', views.convert),
    url(r'^suggest_currency/$', views.suggest_currency, name='suggest_currency'),
    url(r'^calculate/$', views.ajaxcalc),
    url(r'^submit_review/$', views.review_handler),
    url(r'^upload/$', views.file_upload),
    url(r'^upload/$', views.upload_success, name='success'),
    url(r'^retrieve_rates/$', views.load_results)
#    url(r'^comparefx/$', views.comparefx)
    ]