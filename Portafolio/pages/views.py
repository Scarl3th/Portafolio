from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def aboutme(request):
    return render(request,"aboutme.html",{})

def education(request):
    return render(request, "education.html",{})

def projects(request):
    return render(request,"projects.html",{})