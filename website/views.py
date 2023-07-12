from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')

def aboutpage(request):
    return render(request,'aboutme.html')

def contactpage(request):
    return render(request,'contactme.html')