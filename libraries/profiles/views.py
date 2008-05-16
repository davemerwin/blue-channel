"""
Views for creating, editing and viewing site-specific user profiles.

"""

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from profiles import utils


def create_profile(request, form_class=None, success_url=None,
                   template_name='profiles/create_profile.html'):
    """
    Create a profile for the current user, if one doesn't already
    exist.
    
    If the user already has a profile, as determined by
    ``request.user.get_profile()``, a redirect will be issued to the
    :view:`profiles.views.edit_profile` view. If no profile model has
    been specified in the ``AUTH_PROFILE_MODULE`` setting,
    ``django.contrib.auth.models.SiteProfileNotAvailable`` will be
    raised.
    
    To specify the form class used for profile creation, pass it as
    the keyword argument ``form_class``; if this is not supplied, it
    will fall back to a ``ModelForm`` for the model specified in the
    ``AUTH_PROFILE_MODULE`` setting.
    
    If you are supplying your own form class, it must define a method
    named ``save()`` which corresponds to the signature of ``save()``
    on ``ModelForm``, because this view will call it with
    ``commit=False`` and then fill in the relationship to the user
    (which must be via a field on the profile model named ``user``, a
    requirement already imposed by ``User.get_profile()``) before
    finally saving the profile object. If many-to-many relations are
    involved, the convention established by ``ModelForm`` of
    looking for a ``save_m2m()`` method on the form is used, and so
    your form class should define this method.
    
    To specify a URL to redirect to after successful profile creation,
    pass it as the keyword argument ``success_url``; this will default
    to the URL of the :view:`profiles.views.profile_detail` view for
    the new profile if unspecified.
    
    To specify the template to use, pass it as the keyword argument
    ``template_name``; this will default to
    :template:`profiles/create_profile.html` if unspecified.
    
    Context:
    
        form
            The profile-creation form.
    
    Template:
    
        ``template_name`` keyword argument, or
        :template:`profiles/create_profile.html`.
    
    """
    try:
        profile_obj = request.user.get_profile()
        return HttpResponseRedirect(reverse('profiles_edit_profile'))
    except ObjectDoesNotExist:
        pass
    if success_url is None:
        success_url = reverse('profiles_profile_detail',
                              kwargs={ 'username': request.user.username })
    if form_class is None:
        form_class = utils.get_profile_form()
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            profile_obj = form.save(commit=False)
            profile_obj.user = request.user
            profile_obj.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            return HttpResponseRedirect(success_url)
    else:
        form = form_class()
    return render_to_response(template_name,
                              { 'form': form },
                              context_instance=RequestContext(request))
create_profile = login_required(create_profile)

def edit_profile(request, form_class=None, success_url=None,
                 template_name='profiles/edit_profile.html'):
    """
    Edit the current user's profile.
    
    If the user does not already have a profile (as determined by
    ``User.get_profile()``), a redirect will be issued to the
    :view:`profiles.views.create_profile` view; if no profile model
    has been specified in the ``AUTH_PROFILE_MODULE`` setting,
    ``django.contrib.auth.models.SiteProfileNotAvailable`` will be
    raised.
    
    To specify the form class used for profile editing, pass it as the
    keyword argument ``form_class``; this form class must have a
    ``save()`` method which will save updates to the profile
    object. If not supplied, this will default to
    a ``ModelForm`` for the profile model.
    
    If you supply a form class, its ``__init__()`` method must accept
    an instance of the profile model as the keyword argument
    ``instance``.
    
    To specify the URL to redirect to following a successful edit,
    pass it as the keyword argument ``success_url``; this will default
    to the URL of the :view:`profiles.views.profile_detail` view if
    not supplied.
    
    To specify the template to use, pass it as the keyword argument
    ``template_name``; this will default to
    :template:`profiles/edit_profile.html` if not supplied.
    
    Context:
    
        form
            The form for editing the profile.
        
        profile
            The user's current profile.
    
    Template:
    
        ``template_name`` keyword argument or
        :template:`profiles/edit_profile.html`.
    
    """
    try:
        profile_obj = request.user.get_profile()
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('profiles_create_profile'))
    if success_url is None:
        success_url = reverse('profiles_profile_detail',
                              kwargs={ 'username': request.user.username })
    if form_class is None:
        form_class = utils.get_profile_form()
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=profile_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(success_url)
    else:
        form = form_class(instance=profile_obj)
    return render_to_response(template_name,
                              { 'form': form,
                                'profile': profile_obj, },
                              context_instance=RequestContext(request))
edit_profile = login_required(edit_profile)

def profile_detail(request, username, public_profile_field=None,
                   template_name='profiles/profile_detail.html'):
    """
    Detail view of a user's profile.
    
    If no profile model has been specified in the
    ``AUTH_PROFILE_MODULE`` setting,
    ``django.contrib.auth.models.SiteProfileNotAvailable`` will be
    raised.

    If the user has not yet created a profile, ``Http404`` will be
    raised.

    If a field on the profile model determines whether the profile can
    be publicly viewed, pass the name of that field (as a string) as
    the keyword argument ``public_profile_field``; that attribute will
    be checked before displaying the profile, and if it does not
    return a ``True`` value, the ``profile`` variable in the template
    will be ``None``. As a result, this field must be a
    ``BooleanField``.
    
    To specify the template to use, pass it as the keyword argument
    ``template_name``; this will default to
    :template:`profiles/profile_detail.html` if not supplied.
    
    Context:
    
        profile
            The user's profile, or ``None`` if the user's profile is
            not publicly viewable (see the note about
            ``public_profile_field`` above).
    
    Template:
    
        ``template_name`` keyword argument or
        :template:`profiles/profile_detail.html`.
    
    """
    user = get_object_or_404(User, username=username)
    try:
        profile_obj = user.get_profile()
    except ObjectDoesNotExist:
        raise Http404
    if public_profile_field is not None and \
       not getattr(profile_obj, public_profile_field):
        profile_obj = None
    return render_to_response(template_name,
                              { 'profile': profile_obj },
                              context_instance=RequestContext(request))

def profile_list(request, public_profile_field=None,
                 template_name='profiles/profile_list.html', **kwargs):
    """
    List of user profiles.
    
    If no profile model has been specified in the
    ``AUTH_PROFILE_MODULE`` setting,
    ``django.contrib.auth.models.SiteProfileNotAvailable`` will be
    raised.
    
    If a field on the profile model determines whether the profile can
    be publicly viewed, pass the name of that field as the keyword
    argument ``public_profile_field``; the ``QuerySet`` of profiles
    will be filtered to include only those on which that field is
    ``True`` (as a result, this field must be a ``BooleanField``).
    
    This view is a wrapper around the
    :view:`django.views.generic.list_detail.object_list` generic view,
    so any arguments which are legal for that view will be accepted,
    with the exception of ``queryset``, which will always be set to
    the default ``QuerySet`` of the profile model, optionally filtered
    as described above.
    
    Template:
    
        ``template_name`` keyword argument or
        :template:`profiles/profile_list.html`.
    
    Context:
    
        Same as the :view:`django.views.generic.list_detail.object_list`
        generic view.
    
    """
    profile_model = utils.get_profile_model()
    if 'queryset' in kwargs:
        del kwargs['queryset']
    queryset = profile_model._default_manager.all()
    if public_profile_field is not None:
        queryset = queryset.filter(**{ public_profile_field: True })
    return object_list(request,
                       queryset=queryset,
                       template_name=template_name,
                       **kwargs)
