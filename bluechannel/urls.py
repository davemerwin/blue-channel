import os
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template, redirect_to
from django.contrib import admin
from django.views.generic.list_detail import object_detail, object_list
from bluechannel.page.models import *

admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment this for admin:
    (r'^admin/(.*)', admin.site.root),
    
    # For the profiles for users
    (r'^profiles/', include('profiles.urls')),
    
    # Page Detail
    (r'(?P<slug>[-\w]+)/$', 'bluechannel.page.views.detail'),
   
    #for homepage - testing
    (r'^$', 'bluechannel.page.views.home'),
    
    # Creates Site Maps
    # (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

# For Static Content Locally - Do Not Use In Production!
if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '/Users/dave/sandbox/blue-channel/media/'})
    )

