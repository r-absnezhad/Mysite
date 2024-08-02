from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        next_url = request.GET.get('next', '/')
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', '/'))                   
                    return HttpResponseRedirect(next_url)
                    #return redirect('/')
        else:
            form = AuthenticationForm()

        content = {'form':form , 'next': next_url}
        return render(request,'accounts/login.html',content)
    else:
        return redirect('/')


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                #return reverse('accounts:login')
                return redirect('/')
        else:    
            form = UserCreationForm()     
            context = {'form':form}
            return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')


