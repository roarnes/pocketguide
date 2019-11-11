from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=25)
    surename = models.CharField(max_length=25)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    type = models.IntegerField()  # {1:flight, 2:accommodation, 3:entertainment}
    time_begin = models.DateTimeField('booking time begin')
    time_end = models.DateTimeField('booking time end')
    location = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)