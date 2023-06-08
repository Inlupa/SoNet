from django import forms
from .models import *

from django.utils.timezone import now

class OfferInfoForm(forms.ModelForm):
    """Форма отправки данных в базу по тарифу"""
    city = forms.ModelChoiceField(queryset=Cities.objects.all())
    region = forms.ModelChoiceField(queryset=Regions.objects.all())
    class Meta:
        # переписать таблицу
        model = OfferInfo
        fields = ['user_id', 'region', 'adress', 'phone_number','city', 'name', 'tariff_info', 'date']
        widgets = {
            'region': forms.Select(attrs={'class': 'input_offer', 'placeholder':'Регион'}),
            'city': forms.Select(attrs={'class': 'input_offer', 'placeholder': 'Город'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control input_offer', 'placeholder': 'Номер телефона'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control input_offer', 'placeholder': 'Имя'}),
            'adress':forms.Textarea(attrs={'class': 'form-control input_offer', 'type': 'text', 'placeholder': 'Введите ваш адрес' }),
        }
        labels = {
            'name':'Ваше имя',
            'region': 'Регион',
            'city': 'Город:',
            'phone_number': 'Телефон',
            'adress': 'Адрес',
        }


class HostingConfigureForm(forms.ModelForm):
    """Форма отправки данных в базу по тарифу"""
    region = forms.ModelChoiceField(queryset=Regions.objects.all())
    pull = forms.ModelChoiceField(queryset=Pulls.objects.all())
    processor = forms.ModelChoiceField(queryset=Processors.objects.all())
    ram = forms.ModelChoiceField(queryset=Ram.objects.all())
    city = forms.ModelChoiceField(queryset=Cities.objects.all())

    server_name = models.CharField(max_length=100)
    oper_sys = models.CharField(max_length=100)

    traffic = models.CharField(max_length=100)
    tariff_plan = models.CharField(max_length=100)

    class Meta:
        # переписать таблицу
        model = HostingConfigure
        fields = ['pull', 'processor', 'ram', 'user_id', 'region', 'adress', 'phone_number','city', 'name', 'tariff_info', 'date']
        widgets = {
            'region': forms.Select(),
            'pull': forms.Select(attrs={'class': 'offer__select', 'placeholder': 'Пул'}),
            'ram': forms.Select(attrs={'class': 'offer__select', 'placeholder': 'Оперативная память'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control input_offer', 'placeholder': 'Номер телефона'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control input_offer', 'placeholder': 'Имя'}),
            'adress': forms.Textarea(
                attrs={'class': 'form-control input_offer', 'type': 'text', 'placeholder': 'Введите ваш адрес'}),

        }








