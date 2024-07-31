from . import views
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    # login
    path('login',views.login_view,name='login'),
    # logout
    path('logout',views.logout_view,name='logout'),
    # register / signup
    path('signup',views.signup_view,name='signup'),
]    