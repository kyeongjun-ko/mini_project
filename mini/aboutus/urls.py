from django.urls import path, include 
from . import views 

app_name = 'aboutus' 

urlpatterns = [
    path('index',views.index)
    ]

