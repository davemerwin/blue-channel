from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail, object_list
from page.models import Event

event_dict = {
    'queryset': Event.objects.order_by('name'),
    'paginate_by': 25,
}

event_detail = {
    'queryset': Event.objects.all(),
}

urlpatterns = patterns('',
    
    # For the events
    (r'(?P<slug>[-\w]+)/$', object_detail, dict(event_detail, slug_field='slug')),
    (r'^$', object_list, event_dict),

)