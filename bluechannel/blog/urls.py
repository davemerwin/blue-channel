from django.conf.urls.defaults import *
from blog.models import Post

list_dict = {
    'queryset': Post.objects.filter(status='publish'),
    'date_field': 'created_at',
    'paginate_by': 25,
}

latest_dict = {
    'queryset': Post.objects.filter(status='publish'),
    'date_field': 'created_at',
}

detail_dict = {
    'queryset': Post.objects.filter(status='publish'),
    'date_field': 'created_at',
}

urlpatterns = patterns('django.views.generic.date_based',
   url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', detail_dict, name="detail"),
   url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day',   list_dict, name="day-archive"),
   url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', list_dict, name="month-archive"),
   url(r'^(?P<year>\d{4})/$', 'archive_year',  list_dict, name="year-archive"),
   url(r'^$', 'archive_index', latest_dict, name="latest"),
)
