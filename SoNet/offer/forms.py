from django import forms
from .models import *

from django.utils.timezone import now

class OfferInfoForm(forms.ModelForm):
    city = forms.ChoiceField(choices=cities)
    region = forms.ChoiceField(choices=regions)
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



