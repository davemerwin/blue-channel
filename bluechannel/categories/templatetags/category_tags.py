from django import template
from categories.models import Category

register = template.Library()
    
@register.inclusion_tag('itags/category_list.html')
def show_categories():
    category_list = Category.objects.all()
    return {'category_list': category_list}