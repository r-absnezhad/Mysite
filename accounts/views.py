from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user) 
                    return redirect('/')
        form = AuthenticationForm()
        content = {'form':form}
        return render(request,'accounts/login.html',content)
    else:
        return redirect('/')


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    return render(request,'accounts/signup.html')

