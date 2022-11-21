from django import forms
from .models import OfferInfo, regions, cities

class OfferInfoForm(forms.ModelForm):
    city = forms.ChoiceField(choices=cities)
    region = forms.ChoiceField(choices=regions)
    class Meta:
        # переписать таблицу
        model = OfferInfo
        fields = ['user_id', 'region', 'adress', 'phone_number','city', 'name']
        widgets = {
            'region': forms.Select(attrs={'class': 'input_offer', 'placeholder':'Регион'}),
            'city': forms.Select(attrs={'class': 'input_offer', 'placeholder': 'Город'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control input_offer', 'placeholder': 'Номер телефона'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control input_offer', 'placeholder': 'Имя'}),
            'adress': forms.Textarea(attrs={'class': 'form-control input_offer', 'type': 'text', 'placeholder': 'Адрес'}),
        }
        labels = {
            'region': 'Регион',
            'city': 'Город:',
            'phone_number': 'Номер телефона',
            'adress': 'Адрес',
        }

