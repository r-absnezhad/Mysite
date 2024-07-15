from django.shortcuts import render
from website.models import Contact
from website.forms import NameForm,ContactForm
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index_view(request):
    return render(request,'website/index.html')

def contact_view(request):
    return render(request,'website/contact.html')

def about_view(request):
    return render(request,'website/about.html')

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