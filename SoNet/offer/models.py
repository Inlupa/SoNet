from django.db import models
import uuid
# тут надо добвать тупл для дальнейшего селекта

regions =(
    ("Москва", "Москва"),
    ("Московская область", "Московская область"),
    ("Санкт-Петербург", "Санкт-Петербург"),
    ("Ленинградская область", "Ленинградская область"),
)


cities =(
    ("Москва", "Москва"),
    ("Санкт-Петербург", "Санкт-Петербург"),
)

# модель заявки на подключние
class OfferInfo(models.Model):
    user_id = models.IntegerField()
    region = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    offer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    tariff_info = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):

        return self.tariff_info


class TariffsInternet(models.Model):
    name = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    sale = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class TariffsInternetHouse(models.Model):
    name = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    sale = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class TariffsInternetTv(models.Model):
    name = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    channels = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    sale = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True)

    def __str__(self):

        return self.name


class TariffsInternetTvHouse(models.Model):
    name = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    channels = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    sale = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class TariffsTv(models.Model):
    name = models.CharField(max_length=100)
    channels= models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    sale = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
