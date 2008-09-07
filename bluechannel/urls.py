import os
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template, redirect_to
from django.contrib import admin
from django.views.generic.list_detail import object_detail, object_list
from bluechannel.utils.views import apply_markdown
# from bluechannel.feeds import *

admin.autodiscover()

# feeds = {
#     'latest': LatestEntries,
# }

urlpatterns = patterns('',

    # Uncomment this for admin:
    (r'^admin/(.*)', admin.site.root),
    
    # Triggers the markdown viewer
    url(r'^markdown/preview/$', apply_markdown, name="apply_markdown"),
    
    # For the profiles for users
    url(r'^profiles/', include('profiles.urls')),
    
    # For the events
    url(r'^events/', include('bluechannel.page.urls_event')),
    
    # For the events
    url(r'^blog/', include('bluechannel.blog.urls')),
    
    # For comments
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    #Feeds
    # url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    
    # Page Detail
    url(r'(?P<slug>[-\w]+)/$', 'bluechannel.page.views.detail'),
   
    #for homepage - testing
    url(r'^$', 'bluechannel.page.views.home'),
    
)

# For Static Content Locally - Do Not Use In Production!
if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/../media' % (settings.PROJECT_PATH)})
    )

