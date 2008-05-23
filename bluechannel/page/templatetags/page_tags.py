from django import template
from bluechannel.page.models import Page

register = template.Library()

@register.tag
def get_breadcrumb(parser, token):
    """
    Get all parents of a given page going up the parent chain.  If given a
    context variable, this will put the list of pages in that variable, 
    otherwise they'll be placed in a context variable named `breadcrumb`.
    
    Template::
    
        {% get_breadcrumb for page_object_name [as varname] %}
        
    Example with no variable::
    
        {% get_breadcrumb for page %}
        {% for page in breadcrumb %}
            # ...
        {% endfor %}
    
    Example with variable
    
        {% get_breadcrumb for object as page_list %}
        {% for page in page_list %}
            # ...
        {% endfor %}
    
    """
    bits = token.contents.split()
    len_bits = len(bits)
    if len_bits not in (3, 5):
        raise template.TemplateSyntaxError('%s tag requires either two or four arguments') % bits[0]
    if bits[1] != 'for':
        raise template.TemplateSyntaxError("First argument to %s tag must be 'for'") % bits[0]
    if len_bits > 3 and bits[3] != 'as':
        raise template.TemplateSyntaxError("Third argument to %s tag must be 'as'") % bits[0]

    page_obj_name = bits[2]
    context_var = 'breadcrumb'
    if len_bits == 5:
        context_var = bits[4]
    
    return BreadcrumbNode(page_obj_name, context_var)

class BreadcrumbNode(template.Node):
    def __init__(self, page_obj_name, context_var):
        self.page_obj_name = template.Variable(page_obj_name)
        self.context_var = context_var
    
    def render(self, context):
        try:
            page = self.page_obj_name.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        
        page_list = page.get_all_parents()
        context[self.context_var] = page_list
        return ''

        from bluechannel.content.models import *
        from bluechannel.event.models import *
        from bluechannel.asset.models import *
        from django import template

        register = template.Library()

@register.inclusion_tag('includes/page_list.html')
def show_page_list():
    """
    For creating a nav list
    """
    page_list = Page.objects.filter(in_nav=1)
    return {'page_list': page_list}

@register.inclusion_tag('includes/random_testimonial.html')
def show_random_testimonial():
    """
    For generating a single piece of content from content tagged testimonial
    """
    random_testimonial = Content.objects.filter(tags='testimonial').order_by('?')[0]
    return {'random_testimonial': random_testimonial}