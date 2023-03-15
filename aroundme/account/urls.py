from django.contrib import admin
from django.urls import path
from account.views import *
urlpatterns = [
    path('',home.as_view()),
    path('signup/',Signup.as_view(),name="signup"),
    path('log1/',loginview.as_view(),name="login"),
    path('logout/',logout.as_view(),name='lgout'),
    
    
    
    
]
