# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from . import views


urlpatterns = [
    path('accounts/profile/', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('signin', views.Signin.as_view(), name='signin'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('logout/', views.Logout.as_view(), name='logout'),
]