from django.shortcuts import render

# Create your views here.
def INDEX(request):
    return render(request,'Home/Index.html')
def ABOUTME(request):
    return render(request,'Home/Aboutme.html')
def CONTACT(request):
    return render(request,'Home/Contact.html')
def GALLERY(request):
    return render(request,'Home/Gallery.html')
def SERVICES(request):
    return render(request,'Home/services.html')

