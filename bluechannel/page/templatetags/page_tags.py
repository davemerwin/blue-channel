from django import template
from bluechannel.page.models import Page, Highlight

register = template.Library()

@register.tag
def get_breadcrumb(parser, token):
	"""
	Get all parents of a given page going up the parent chain.	If given a
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

		from bluechannel.highlight.models import *
		from bluechannel.event.models import *
		from bluechannel.asset.models import *
		from django import template

		register = template.Library()

@register.inclusion_tag('itags/page_list.html')
def show_page_list():
	"""
	For creating a nav list
	"""
	page_list = Page.objects.filter(in_nav=1).order_by('order')
	return {'page_list': page_list}
	
@register.inclusion_tag('itags/about_blurb.html')
def about_blurb():
	"""
	For creating a nav list
	"""
	about_blub = Highlight.objects.filter(tags='about-blurb')
	return {'about_blurb': about_blurb}
	
@register.inclusion_tag('itags/page_list_accessible.html')
def show_page_list_accessible():
	"""
	For creating a nav list
	"""
	page_list = Page.objects.filter(in_nav=1).order_by('order')
	return {'page_list': page_list}

@register.inclusion_tag('itags/random_testimonial.html')
def show_random_testimonial():
	"""
	For generating a single piece of content from content tagged testimonial
	"""
	random_testimonial = Highlight.objects.filter(tags='testimonial')
	if random_testimonial != '':
		return {'random_testimonial': random_testimonial}
	else:
		return 'Nothing Here'

@register.inclusion_tag('itags/home_detail.html')
def show_home_detail():
	"""
	For generating a single piece of content from pages
	"""
	home_detail = Page.objects.filter(is_home=1)
    
	if home_detail != '':
	    return {'home_detail': home_detail}
	else:
	    return ''

@register.inclusion_tag('itags/events_list.html')
def show_events_list():
	"""
	For showing pages tagged with events
	"""
	events_list = Page.objects.filter(tags='events').order_by('-created')
	return {'events_list': events_list}
	
@register.inclusion_tag('itags/blog_list.html')
def show_blog_list():
	"""
	For showing pages tagged with events
	"""
	blog_list = Page.objects.filter(page_type=3).order_by('-created')[:4]
	return {'blog_list': blog_list}

@register.inclusion_tag('itags/news_list.html')
def show_news_list():
	"""
	For showing pages tagged with events
	"""
	news_list = Page.objects.filter(tags='news').order_by('-created')
	return {'news_list': news_list}
	
@register.inclusion_tag('itags/did_you_know.html')
def get_did_you_know():
	"""
	For showing content tagged with dyk (did you know)
	"""
	did_you_know = Highlight.objects.filter(tags='dyk').order_by('?')
	if did_you_know != '':
		return {'did_you_know': did_you_know}
	else:
		return ''

@register.inclusion_tag('itags/sub_menu.html')
def get_submenu():
	"""
	Show Siblings of the current page and all children
	"""	
	siblings = Page.get_all_siblings()
	#children = Page.objects.filter(parent=self.id)
	return {'siblings': siblings}