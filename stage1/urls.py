from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.zuri_api, name='zuri'),
]