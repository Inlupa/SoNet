
from django.db import models


class News(models.Model):
    object_id = models.IntegerField(primary_key=True)
    some_text = models.CharField(max_length=-1, blank=True, null=True)
    news_anno = models.CharField(max_length=-1)
    pub_date = models.DateField()
    news_name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'news'
