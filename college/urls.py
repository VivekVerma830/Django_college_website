from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('course/',course,name='course'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),

  
]