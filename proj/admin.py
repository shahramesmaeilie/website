from django.contrib import admin
from . import models
import os
# Register your models here.
class list1(admin.ModelAdmin):
    list_display=('code','nam','modir','title')
    list_filter=('code','nam')
    search_fields=('code','modir')
admin.site.register(models.TITLE)
admin.site.register(models.PROJECT,list1)