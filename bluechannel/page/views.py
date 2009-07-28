from django.db import models
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail

Page = models.get_model('page', 'page')

# see docs for how to grab the template view. Pretty straight forward

def page_list(request): #For now lists ALL pages
    page_list = Page.objects.all()
    return object_list(request, queryset=page_list) # the name is the class to generic view to return with the query set
    
def published_page(request, slug):
    slug_field=slug
    published_page = Page.objects.filter(status='Publish')
    return object_detail(request, slug=slug_field, queryset=published_page)

def detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    template = page.template or 'page/page_detail.html'
    return render_to_response(
        template,
        {'object': page},
        context_instance=RequestContext(request)
    )
    
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
