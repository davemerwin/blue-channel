from django import template
from bluechannel.blog.models import Post

register = template.Library()

@register.inclusion_tag('itags/blog_recent_list.html')
def recent_entries_list():
    """Recent Blog Entries"""
    recent_list = Post.objects.order_by('-created_at')[:5]
    return {'recent_list': recent_list}
    
@register.inclusion_tag('itags/blog_archive_list.html')
def show_archive_blog():
    archive_list = Post.objects.all()
    return {'archive_list': archive_list}
