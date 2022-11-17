from django.contrib import admin
from .models import Car
# , TripCategory, Destination
#python3 manage.py createsuperuser
# Register your models here.
admin.site.register(Car)
# admin.site.register(TripCategory)
# admin.site.register(Destination)