from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import OfferInfoForm


def internet_tv(request):
    offer_form = OfferInfoForm(request.POST)
    if request.method == 'POST':
        #если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.save()
    return render(request,'offer/internet_tv.html', context={'offer_form':offer_form})


def internet(request):
    offer_form = OfferInfoForm(request.POST)
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.save()
    return render(request,'offer/internet.html', context={'offer_form':offer_form})

def tv(request):
    offer_form = OfferInfoForm(request.POST)
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.save()
    return render(request,'offer/tv.html', context={'offer_form':offer_form})

def hosting(request):
    offer_form = OfferInfoForm(request.POST)
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.save()
    return render(request,'offer/hosting.html', context={'offer_form':offer_form})