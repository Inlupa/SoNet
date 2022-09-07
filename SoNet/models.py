# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class News(models.Model):
    object_id = models.IntegerField(primary_key=True)
    some_text = models.CharField(max_length=-1, blank=True, null=True)
    news_anno = models.CharField(max_length=-1)
    pub_date = models.DateField()
    news_name = models.CharField(max_length=-1)
    news_url = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'
