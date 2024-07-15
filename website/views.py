from django.shortcuts import render
from website.models import Contact
from website.forms import NameForm
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
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(name, email, subject, message)
            return HttpResponse('done')
        else:
            return HttpResponse(' not done ')
    form = NameForm()    
    return render(request,'test.html',{'form':form})