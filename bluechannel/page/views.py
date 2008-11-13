from django.views.generic.list_detail import *
from page.models import *
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.views.generic.list_detail import object_list, object_detail
from django.http import Http404, HttpResponseRedirect

# see docs for how to grab the template view. Pretty straight forward

def page_list(request): #For now lists ALL pages
    page_list = Page.objects.all()
    return object_list(request, queryset=page_list) # the name is the class to generic view to return with the query set
    
def published_page(request, slug):
    slug_field=slug
    published_page = Page.objects.filter(status='Publish')
    return object_detail(request, slug=slug_field, queryset=published_page)

def detail(request, slug):
    return object_detail(request, slug=slug, queryset=Page.published_objects.all())
    
def home(request):
    try:
        home = Page.published_objects.get(is_home=True)
    except Page.DoesNotExist:
	home = None
        
    return render_to_response(
        'page/homepage.html',
        {'home': home,},
        context_instance=RequestContext(request)
    )