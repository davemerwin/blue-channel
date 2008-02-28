"""
URLConf for Django user profile management.

Recommended usage is to use a call to ``include()`` in your project's
root URLConf to include this URLConf for any URL beginning with
'/profiles/'.

"""

from django.conf.urls.defaults import *

from profiles import views


urlpatterns = patterns('',
                       url(r'^create/$',
                           views.create_profile,
                           name='profiles_create_profile'),
                       url(r'^edit/$',
                           views.edit_profile,
                           name='profiles_edit_profile'),
                       url(r'^(?P<username>\w+)/$',
                           views.profile_detail,
                           name='profiles_profile_detail'),
                       url(r'^$',
                           views.profile_list,
                           name='profiles_profile_list'),
                       )
