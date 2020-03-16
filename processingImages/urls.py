from django.urls import path, include, re_path
from django.conf.urls import  url
from . import views

urlpatterns = [
     path('index/', views.index, name='index'),
     path('getProcessingImage/', views.getProcessingImage, name='getProcessingImage'),
     path('showNuage/', views.showNuage, name='showNuage'),
     path('', views.getModel,name='getModel')

]
