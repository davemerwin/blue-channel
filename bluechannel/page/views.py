from django.views.generic.list_detail import *
from bluechannel.page.models import *
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.views.generic.list_detail import object_list, object_detail
from django.http import Http404, HttpResponseRedirect

try:
    from xml.etree.ElementTree import Element, SubElement, tostring
except ImportError:
    try:
        from elementtree.ElementTree import Element, SubElement, tostring
    except ImportError:
        raise "This project requires ElementTree to be installed."

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

def generate_menu(req_page, root=None, include_root=True):
    """
    This function returns the menu as a string generated from ElementTree.
    If root is specified, only pulls pages below that root.
    """
    if root:
        if include_root:
            roots = Navigation.objects.select_related().filter(page__number=root)
        else:
            roots = Navigation.objects.select_related().filter(parent__number=root).filter(show_in_menu=True).order_by('page_page.number')
    else:
        # Get all top level pages (pages with no parents)
        roots = Navigation.objects.select_related().filter(parent__isnull=True).filter(show_in_menu=True).order_by('page_page.number')
    if not roots:
        return

    # Get list of parents -- all parents going up the tree from current page
    # We use this to know which children to traverse
    try:
        parent = Navigation.objects.get(page=req_page).parent
    except Navigation.DoesNotExist:
        return []
    all_parents = [req_page,]
    while parent:
        all_parents.append(parent)
        parent = Navigation.objects.get(page=parent).parent

    # Start root UL element
    menu = Element('ul', {'id': 'subNav'})
    # Iterate over root pages, diving into children
    for p in roots:
        href_attrs = {'href': p.page.get_absolute_url()}
        li_attrs = {}
        if p.page in all_parents:
            li_attrs['class'] = 'active' # This is where we are
        sub_menu = SubElement(menu, 'li', li_attrs)
        link = SubElement(sub_menu, 'a', href_attrs)
        link.text = p.page.get_title()
        recurse_for_children(sub_menu, req_page, all_parents, p, 2)

    return tostring(menu, 'utf-8')

def recurse_for_children(menu, req_page, all_parents, cur_nav, level, max_depth=4, breadcrumb=False):
    children = Navigation.objects.select_related().filter(parent=cur_nav.page).filter(show_in_menu=True).order_by('page_page.number')
    if not children:
        return False
    if level > max_depth:
        return False

    if not breadcrumb:
        menu = SubElement(menu, 'ul', {'class': 'subNavMenu'}) # we have children, so make a sublist
    for c in children:
        href_attrs = {'href': c.page.get_absolute_url()}
        li_attrs = {}
        if c.page in all_parents:
            li_attrs['class'] = 'active' # This is where we are
        new_menu = SubElement(menu, 'li', li_attrs)
        link = SubElement(new_menu, 'a', href_attrs)
        link.text = c.page.get_title()

        if not recurse_for_children(new_menu, req_page, all_parents, c, level+1):
            new_menu = menu
