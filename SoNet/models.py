# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OfferInfo(models.Model):
    user_id = models.IntegerField()
    region = models.CharField(max_length=-1)
    adress = models.CharField(max_length=-1)
    phone_number = models.CharField(max_length=-1)
    city = models.CharField(max_length=-1)
    offer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=-1)
    tariff_type = models.CharField(max_length=-1, blank=True, null=True)
    offer_price = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_info'
