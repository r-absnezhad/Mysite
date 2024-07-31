from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        message = f'User is authenticated as {request.user.username}'
    else:
        message = 'User is not authenticated'
    
    return render(request,'accounts/login.html',{'message':message})

#def logout_view(request):
#    pass
def signup_view(request):
    return render(request,'accounts/signup.html')

