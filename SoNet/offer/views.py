from django.shortcuts import render
from django.http import JsonResponse
from .forms import OfferInfoForm
from .models import TariffsInternetTv, TariffsTv, TariffsInternet
import  json


# def get_data(request):
#     name = request.GET.get("tariff", None)
#     price = request.GET.get("price", None)
#     print(name, price)
#     return(JsonResponse({"name":name, 'price':price}))

def take_py(txt_in):
    global txt
    txt = txt_in
    print(txt)


def internet_tv(request):
    offer_form = OfferInfoForm(request.POST)
    tariffs = TariffsInternetTv.objects.all()

    # name = request.GET.get("tariff", None)
    # price = request.GET.get("price", None)
    # print(name, price)
    if request.method == 'POST':
        #если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.save()
            offer_form = OfferInfoForm()
    return render(request,'offer/internet_tv.html', context= {'tariffs': tariffs,'offer_form': offer_form })

#тут надо будет подключить из базы список тарифов которые надо будет выводить на сайт и поддключить к ним калькулятор(3 часа работы, может два часа)
def internet(request):
    offer_form = OfferInfoForm(request.POST)
    tariffs = TariffsInternet.objects.all()
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.save()
    return render(request,'offer/internet.html', context={'tariffs': tariffs, 'offer_form':offer_form})

def tv(request):
    offer_form = OfferInfoForm(request.POST)
    tariffs = TariffsTv.objects.all()
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.save()
    return render(request,'offer/tv.html', context={'tariffs': tariffs, 'offer_form':offer_form})

def hosting(request):
    offer_form = OfferInfoForm(request.POST)
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.save()
    return render(request,'offer/hosting_1.html', context={'offer_form':offer_form})