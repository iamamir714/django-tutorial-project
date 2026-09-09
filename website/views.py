from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) # to process the data
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket was submited successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket was not submited.')

    form = ContactForm() # to display on the page
    return render(request, 'website/contact.html', {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
            form = NewsletterForm(request.POST) # to process the data
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) # to process the data
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
            
    form = ContactForm() # to display on the page
    return render(request, 'test.html', {'form':form})
