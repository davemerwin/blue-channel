# Create your views here.
from django.views.generic.list_detail import *
from bluechannel.page.models import *

# see docs for how to grab the template view. Pretty straight forward

def page_list(request): #For now lists ALL pages
    page_list = Page.objects.all()
    return object_list(request, queryset=page_list) # the name is the class to generic view to return with the query set
    
def published_page(request, slug):
    slug_field=slug
    published_page = Page.objects.filter(status='Publish')
    return object_detail(request, slug=slug_field, queryset=published_page)