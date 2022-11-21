from django.db import models

# тут надо добвать тупл для дальнейшего селекта

regions =(
    ("1", "Москва"),
    ("2", "Московская область"),
    ("3", "Санкт-Петербург"),
    ("4", "Ленинградская область"),
)


cities =(
    ("1", "Москва"),
    ("2", "Санкт-Петербург"),
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

    class Meta:
        managed = False
        db_table = 'offer_info'