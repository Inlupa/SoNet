from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(OfferInfo)

admin.site.register(TariffsTv)
admin.site.register(TariffsInternet)
admin.site.register(TariffsInternetTv)
admin.site.register(TariffsInternetTvHouse)
admin.site.register(TariffsInternetHouse)
admin.site.register(Cities)
admin.site.register(Regions)
admin.site.register(Pulls)
admin.site.register(Ram)
admin.site.register(Processors)
admin.site.register(OperSys)
admin.site.register(HostingConfigure)



