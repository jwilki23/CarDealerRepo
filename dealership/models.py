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
        return (self.make,self.model,self.year)

# class Destination(models.Model):
#     trip_category = models.OneToOneField(TripCategory, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50)
#     days = models.IntegerField(default=0)
#     cost = models.DecimalField(max_digits=8, decimal_places=2)
#     main_photo = models.ImageField(upload_to='photos')
#     is_active = models.BooleanField(default=True)
#     leave_data = models.DateField(default=datetime.today, blank=True)

#     def __str__(self):
#         return (self.title)

# class Customer(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     user_name = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=13, blank=True)
#     destinations = models.ManyToManyField(Destination, blank=True)

#     def __str__(self):
#         return (self.full_name)

#     @property
#     def full_name(self):
#         return '%s %s' % (self.first_name, self.last_name)
    
#     def save(self):
#         self.first_name = self.first_name.upper()
#         self.last_name = self.last_name.upper()
#         super(Customer, self).save()


#python3 manage.py makemigrations
# python3 manage.py migrate
