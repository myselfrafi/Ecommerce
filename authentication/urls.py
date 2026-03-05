from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name='register-form'),
    path('login',views.login,name='login-form'),
    path('home',views.homepage,name='Home-Page'),
    path('logout',views.LogoutView,name='logout'),
] 
    
    