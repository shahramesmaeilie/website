from django.urls import path
from . import views
import os

urlpatterns = [
  
    path('',views.projlist,name='projl'),
    path('formp/',views.projlistf,name='projf'),
    path('add/',views.addproj,name='add'),
    path('search/',views.searchproj,name='search'),
    path('searchc/',views.searchcproj,name='searchc'),
    path('delete/',views.delproj,name='delete'),
]