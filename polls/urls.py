from django.urls import path, include
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:x>/', views.detail_sunhan, name="detail_sunhan"),
    path('where/all', views.where, name="where"),
    path('where/<int:x>', views.where_detail, name="where_detail"),
]
