from django.urls import path, include, url
from django.contrib import admin
from . import views 

app_name = 'miniport' 

urlpatterns = [
    path('detail',views.detail),
    
    ]

