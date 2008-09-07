from django import template
from bluechannel.blog.models import Entry

register = template.Library()

@register.inclusion_tag('itags/blog_recent_list.html')
def recent_entries_list():
    """Recent Blog Entries"""
    recent_list = Entry.objects.order_by('created')[:5]
    return {'recent_list': recent_list}
    
@register.inclusion_tag('itags/blog_archive_list.html')
def show_archive_blog():
    archive_list = Entry.objects.all()
    return {'archive_list': archive_list}