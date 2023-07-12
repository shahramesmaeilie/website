from django.shortcuts import render,redirect
from . import models
from . import forms

# Create your views here.
def projlist(request):
    l=models.PROJECT.objects.all()
    return render(request,'proj/projlist.html',{'l':l})
def projlistf(request):
    l=models.PROJECT.objects.all()
    return render(request,'proj/projlistf.html',{'l':l})
def addproj(request):
    if request.method=="POST":
        form=forms.projform(request.POST,request.FILES)
        if form.is_valid():
           form.save()
           note='اطلاعات وارد شده با نام %s و کد %s ذخیره شد.' % (form.cleaned_data['nam'],form.cleaned_data['code'])
           form1=forms.projform()
        return render(request,'proj/createproj.html',{'form':form1,'note':note})
        #return redirect('projl')
    else:
        form=forms.projform()
    return render(request,'proj/createproj.html',{'form':form})
def searchproj(request):
    q=request.GET.get("t1")
    if q!="":
       l=models.PROJECT.objects.filter(nam=q)
    else:
         l=models.PROJECT.objects.all()
    return render(request,'proj/projlist.html',{'l':l})
def searchcproj(request):
    q=request.GET.get("t2")
    if q!="":
       l=models.PROJECT.objects.filter(code=q)
    else:
         l=models.PROJECT.objects.all()
    return render(request,'proj/searchc.html',{'l':l})
def delproj(request):
    q=request.GET.get("t3")
    ll=models.PROJECT.objects.filter(code=q)
    ll.delete()
    l=models.PROJECT.objects.all()
    return render(request,'proj/projlist.html',{'l':l})