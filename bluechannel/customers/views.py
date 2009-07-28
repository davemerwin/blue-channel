from django.forms import ModelForm
from django.shortcuts import render_to_response
from bluechannel.customers.models import CustomerForm
from django.template import Context, Template, RequestContext
from django.http import Http404, HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# see docs for how to grab the template view. Pretty straight forward

def subscribe(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            
            # Send an email to teh admin letting them know that a person registered
            subject = render_to_string('subscribe/email_subject.txt',)
            message = render_to_string('subscribe/email.txt', {
                    'user': request.user,
                })
            recipients = ['dave.merwin@gmail.com']
            # recipients = ['johnsonlm@wou.edu']
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)
            
            return HttpResponseRedirect('/thanks/')
    else:
        form = CustomerForm()
        
    return render_to_response('subscribe/customer.html', {'form':form}, context_instance=RequestContext(request))
