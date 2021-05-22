from django.db import models

# Create your models here.


class KeyValue(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    uiid = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'key_value'
