from django.contrib import admin
from .models import *
# Register your models here.
class Details(admin.ModelAdmin):
    list_display=['model','name','no','From','To','Departure','Date','price']
admin.site.register(FlightDetails)

