from django.conf.urls.defaults import *
from blog.models import Post

info_dict = {
    'queryset': Post.objects.filter(status='publish'),
    'date_field': 'created',
    #'paginate_by': 25,
}

urlpatterns = patterns('django.views.generic.date_based',
   url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', info_dict, name="detail"),
   url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day',   info_dict, name="day-archive"),
   url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', info_dict, name="month-archive"),
   url(r'^(?P<year>\d{4})/$', 'archive_year',  info_dict, name="year-archive"),
   url(r'^$', 'archive_index', info_dict, name="latest"),
)
