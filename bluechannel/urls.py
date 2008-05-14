from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic.list_detail import object_detail, object_list
from bluechannel.settings import PROJECT_PATH, DEBUG
import os

urlpatterns = patterns('',
    # Example:
    # (r'^bluechannel/', include('bluechannel.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    
    # For the profiles for users
    (r'^profiles/', include('profiles.urls')),
    
    # Page Detail
    #(r'^(?P<slug>[-\w]+)/$', section_base),
    
    #for homepage - testing
    #(r'^$', direct_to_template, {'template': 'homepage.html'}),
    
    # Creates Site Maps
    # (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

# For Static Content Locally - Do Not Use In Production!
if DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root':'/Users/dave/sandbox/icarus/media/'})
    )

