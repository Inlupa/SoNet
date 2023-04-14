from django.shortcuts import render
from .forms import OfferInfoForm
from .models import TariffsInternetTv, TariffsTv, TariffsInternet, TariffsInternetTvHouse, TariffsInternetHouse
import datetime
from django.core.mail import send_mail, EmailMessage



def internet_tv(request):
    offer_form = OfferInfoForm(request.POST)
    tariffs = TariffsInternetTv.objects.all()
    tariffs_house = TariffsInternetTvHouse.objects.all()
    if request.method == 'POST':
        #если юзер заел в профиль то подтянуть айди и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.instance.user_id = request.user.id

            now = datetime.datetime.now()
            offer_form.instance.date = now


            text_mail =  'Вы подали заявку на подключение от: ' + str(now)
            email = EmailMessage(
                    "Заявка",
                    text_mail,
                    'msu_hydro70@mail.ru',
                    [request.user.email])
            email.send()

            offer_form.save()
            offer_form = OfferInfoForm()
    return render(request,'offer/internet_tv.html', context= {'tariffs': tariffs, 'tariffs_house': tariffs_house,'offer_form': offer_form })

#тут надо будет подключить из базы список тарифов которые надо будет выводить на сайт и поддключить к ним калькулятор(3 часа работы, может два часа)
def internet(request):
    offer_form = OfferInfoForm(request.POST)

    tariffs = TariffsInternet.objects.all()
    tariffs_house = TariffsInternetHouse.objects.all()
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.instance.user_id = request.user.id

            now = datetime.datetime.now()
            offer_form.instance.date = now

            text_mail = 'Вы подали заявку на подключение от: ' + str(now)
            email = EmailMessage(
                "Заявка",
                text_mail,
                'msu_hydro70@mail.ru',
                [request.user.email])
            email.send()

            offer_form.save()
            offer_form = OfferInfoForm()
    return render(request,'offer/internet.html', context={'tariffs': tariffs,'tariffs_house': tariffs_house, 'offer_form':offer_form})

def tv(request):
    offer_form = OfferInfoForm(request.POST)
    tariffs = TariffsTv.objects.all()
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.instance.user_id = request.user.id
            now = datetime.datetime.now()
            offer_form.instance.date = now

            text_mail = 'Вы подали заявку на подключение от: ' + str(now)
            email = EmailMessage(
                "Заявка",
                text_mail,
                'msu_hydro70@mail.ru',
                [request.user.email])
            email.send()


            offer_form.save()
            offer_form = OfferInfoForm()
    return render(request,'offer/tv.html', context={'tariffs': tariffs, 'offer_form':offer_form})

def hosting(request):
    offer_form = OfferInfoForm(request.POST)
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди  и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.instance.user_id = request.user.id
            now = datetime.datetime.now()
            offer_form.instance.date = now

            text_mail = 'Вы подали заявку на подключение от: ' + str(now)
            email = EmailMessage(
                "Заявка",
                text_mail,
                'msu_hydro70@mail.ru',
                [request.user.email])
            email.send()

            offer_form.save()
            offer_form = OfferInfoForm()
    return render(request,'offer/hosting_1.html', context={'offer_form':offer_form})


def hosting_stoiko(request):
    offer_form = OfferInfoForm(request.POST)
    if request.method == 'POST':
        # если юзер заел в профиль то подтянуть айди и сотальные данные из базы, если нет то надо
        offer_form = OfferInfoForm(request.POST)
        if offer_form.is_valid():
            offer_form.instance.user_id = request.user.id
            now = datetime.datetime.now()
            offer_form.instance.date = now

            text_mail = 'Вы подали заявку на подключение от: ' + str(now)
            email = EmailMessage(
                "Заявка",
                text_mail,
                'msu_hydro70@mail.ru',
                [request.user.email])
            email.send()

            offer_form.save()
            offer_form = OfferInfoForm()
    return render(request,'offer/hosting_2.html', context={'offer_form':offer_form})