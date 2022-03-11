from django.urls import path, include 
from . import views 

app_name = 'miniport' 

urlpatterns = [
    path('detail',views.detail)
    ]

