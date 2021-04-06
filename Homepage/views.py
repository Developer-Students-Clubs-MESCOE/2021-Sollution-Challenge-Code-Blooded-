from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "homepage/homepage.html")

def contactUs(request):
    return render(request, "homepage/contact.html")
