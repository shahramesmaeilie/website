from django.urls import path
from . import views
import os

urlpatterns = [
    path('',views.INDEX,name='index'),
    path('aboutme/',views.ABOUTME,name='aboutme'),
    path('contact/',views.CONTACT,name='contact'),
    path('gallery/',views.GALLERY,name='gallery'),
    path('services/',views.SERVICES,name='services'),
]