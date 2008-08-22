import os
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template, redirect_to
from django.contrib import admin
from django.views.generic.list_detail import object_detail, object_list
from bluechannel.page.models import *
from bluechannel.utils.views import apply_markdown

admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment this for admin:
    (r'^admin/(.*)', admin.site.root),
    
    # Triggers the markdown viewer
    url(r'^markdown/preview/$', apply_markdown, name="apply_markdown"),
    
    # For the profiles for users
    url(r'^profiles/', include('profiles.urls')),
    
    # Page Detail
    url(r'(?P<slug>[-\w]+)/$', 'bluechannel.page.views.detail'),
   
    #for homepage - testing
    url(r'^$', 'bluechannel.page.views.home'),
    
    # Creates Site Maps
    # (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
    
)

# For Static Content Locally - Do Not Use In Production!
if settings.DEBUG:
    urlpatterns += patterns('', 
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': '/Users/dave/sandbox/blue-channel/media/'})
    )

