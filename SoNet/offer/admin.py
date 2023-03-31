from django.contrib import admin

# Register your models here.
from .models import OfferInfo, TariffsTv, TariffsInternet, TariffsInternetTv

admin.site.register(OfferInfo)

admin.site.register(TariffsTv)
admin.site.register(TariffsInternet)
admin.site.register(TariffsInternetTv)
