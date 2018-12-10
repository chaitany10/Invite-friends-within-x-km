from django.db import models


# Create your models here.
class Entry(models.Model):
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)
    name = models.CharField(max_length=20)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name


