from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    path('about/',views.aboutpage,name='about'),
    path('contact/',views.contactpage,name='contact'),
    path('proj/',include('proj.urls')),
    path('account/',include('account.urls')),
    path('Home/',include('Home.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)