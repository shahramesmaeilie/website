from django import forms
from . import models
class projform(forms.ModelForm):
    class Meta:
        model=models.PROJECT
        fields='__all__'
        labels={'code':'کد پروژه','nam':'نام پروژه','cost':'هزینه پروژه','duration':'مدت زمان پروژه',
                'modir':'مدیر پروژه','place':'محل پروژه','pic':'تصویر پروژه',
                'status':'وضعیت','desc':'توضیحات','teedadnafar':'تعداد نفرات','title':'موضوع پروژه'}