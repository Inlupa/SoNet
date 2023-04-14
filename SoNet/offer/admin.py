from django.contrib import admin

# Register your models here.
from .models import OfferInfo, TariffsTv, TariffsInternet, TariffsInternetTv, TariffsInternetTvHouse, TariffsInternetHouse

admin.site.register(OfferInfo)

admin.site.register(TariffsTv)
admin.site.register(TariffsInternet)
admin.site.register(TariffsInternetTv)
admin.site.register(TariffsInternetTvHouse)
admin.site.register(TariffsInternetHouse)
