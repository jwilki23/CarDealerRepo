from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    mileage = models.IntegerField(default=0)
    cleanTitle = models.BooleanField(default=True)


    def __str__(self):
        return '%s %s %s' %(self.make,self.model,str(self.year))

