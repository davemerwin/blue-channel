from django.conf.urls.defaults import *
from bluechannel.blog.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'created',
    #'paginate_by': 25,
}

urlpatterns = patterns('django.views.generic.date_based',
   (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', info_dict),
   (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',               'archive_day',   info_dict),
   (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                                'archive_month', info_dict),
   (r'^(?P<year>\d{4})/$',                                                    'archive_year',  info_dict),
   (r'^$',                                                                    'archive_index', info_dict),
)
