import os
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic.list_detail import object_detail, object_list
from bluechannel.page.models import *

info_dict = {
    'queryset': Page.objects.filter(status='Publish'),
}

urlpatterns = patterns('',

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    
    # For the profiles for users
    (r'^profiles/', include('profiles.urls')),
    
    # Page Detail
    (r'(?P<slug>[-\w]+)/$', 'bluechannel.page.views.detail'),
    #(r'(?P<slug>[-\w]+)/$', 'bluechannel.page.views.published_page'),
    #(r'(?P<slug>[-\w]+)/$', object_detail, info_dict),    
    #for homepage - testing
    (r'^$', direct_to_template, {'template': 'page/homepage.html'}),
    
    # Creates Site Maps
    # (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

# For Static Content Locally - Do Not Use In Production!
if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/../media' % (settings.PROJECT_PATH)})
    )

