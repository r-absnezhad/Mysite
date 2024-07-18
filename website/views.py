from django.shortcuts import render
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def index_view(request):
    return render(request,'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'YOU DID IT CORRECTLY')
        else:
            messages.add_message(request,messages.ERROR,"YOU DIDN'T DO IT CORRECTLY")
    form = ContactForm()        
    return render(request,'website/contact.html',{'form':form})

def about_view(request):
    return render(request,'website/about.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')




def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse(' not done ')
    form = ContactForm()    
    return render(request,'test.html',{'form':form})