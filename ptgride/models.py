from django.db import models
from bookings.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    location = models.IntegerField()

class PtgBooking(models.Model):
    type = models.IntegerField() # {1:ride 2:car}
    time_begin = models.DateTimeField('booking time begin')
    time_end = models.DateTimeField('booking time end')
    pickup_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='pickup_location')
    dropoff_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='dropoff_location')
    cost = models.IntegerField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)