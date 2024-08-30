from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), 
    path('logout/', views.user_logout, name='logout'),  
    path('register/', views.register, name="register")
]