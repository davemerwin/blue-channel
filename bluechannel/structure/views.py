# Create your views here.
from django.views.generic.list_detail import object_detail
from bluechannel.structure.models import *
from bluechannel.page.models import *

def section_base(request, slug):
    slug_field=slug
    section = Section.objects.filter(slug=slug)
    return object_detail(request, slug=slug_field, queryset=section)