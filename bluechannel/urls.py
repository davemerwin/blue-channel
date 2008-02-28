from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    # Example:
    # (r'^bluechannel/', include('bluechannel.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    
    # For the profiles for users
    (r'^profiles/', include('profiles.urls')),
    
    # Page Detail
    (r'^(?P<slug>[-\w]+)/$', 'bluechannel.page.views.published_page'),
    
    # Creates Site Maps
    # (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

# For Static Content Locally - Do Not Use In Production!
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/dave/sandbox/bluechannel/media'}),
    )
