from django.db import models
# модель для новостей
class News(models.Model):
    object_id = models.IntegerField(primary_key=True)
    some_text = models.CharField(max_length=500, blank=True, null=True)
    news_anno = models.CharField(max_length=100)
    pub_date = models.DateField()
    news_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'news'