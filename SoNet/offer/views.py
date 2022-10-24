from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def internet_tv(request):
    return render(request,'offer/internet_tv.html')

def internet(request):
    return render(request, "offer/internet.html")

def tv(request):
    return render(request, "offer/tv.html")

def hosting(request):
    return render(request, "offer/hosting.html")