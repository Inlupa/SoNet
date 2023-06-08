from django.db import models

class Cities(models.Model):
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=100)
    def __str__(self):
        return self.city_name

class Regions(models.Model):
        region_id = models.IntegerField()
        region_name = models.CharField(max_length=100)
        def __str__(self):
            return self.region_name

class Pulls (models.Model):
        pull_id = models.IntegerField()
        pull_name = models.CharField(max_length=100)
        def __str__(self):
            return self.pull_name

class Processors(models.Model):
        proc_id = models.IntegerField()
        proc_name = models.CharField(max_length=100)
        proc_hz = models.CharField(max_length=100)
        proc_core_number = models.CharField(max_length=100)
        def __str__(self):
            return self.proc_name

class OperSys(models.Model):
    os_id = models.IntegerField()
    os_name = models.CharField(max_length=100)
    os_pic = models.ImageField()

    def __str__(self):
        return self.os_name

class Ram(models.Model):
    ram_id = models.IntegerField()
    ram_size = models.CharField(max_length=100)

    def __str__(self):
        return self.ram_size

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


class HostingConfigure(models.Model):
    user_id = models.IntegerField()
    region = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    offer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    tariff_info = models.CharField(max_length=100, blank=True, null=True)

    server_name = models.CharField(max_length=100)
    oper_sys = models.CharField(max_length=100)
    pull = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)

    traffic = models.CharField(max_length=100)
    tariff_plan = models.CharField(max_length=100)

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
