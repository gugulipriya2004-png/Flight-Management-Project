from django.db import models

# Create your models here.
class FlightDetails(models.Model):
    model=models.TextField(max_length=20,default='Emirates')
    name=models.TextField(max_length=20)
    no=models.IntegerField()
    From=models.TextField(max_length=20)
    To=models.TextField(max_length=20)
    Departure=models.TimeField(max_length=20)
    Date=models.DateField()
    Price=models.IntegerField()

class Book_Details(models.Model):
    model=models.TextField(max_length=20,default='Emirates')
    name=models.TextField(max_length=20)
    no=models.IntegerField()
    From=models.TextField(max_length=20)
    To=models.TextField(max_length=20)
    Departure=models.CharField(max_length=20)
    Date=models.DateField()
    Price=models.IntegerField()
    your_name=models.TextField(max_length=20,default='Emirates')
    Email=models.EmailField(max_length=20)
    Phone_no=models.CharField(max_length=15)
    Adhaar_no=models.IntegerField()
    age=models.IntegerField()
    seat_class=models.TextField(max_length=20,default='Emirates')
    seat_no=models.IntegerField()



