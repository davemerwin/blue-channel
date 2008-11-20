from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'customers.views.subscribe', name='subscribe'),
)
