from django.db import models

# Create your models here.
class Flight(models.Model):
    airline_name = models.CharField(max_length = 256)
    from_city = models.CharField(max_length = 256)
    to_city = models.CharField(max_length = 256)
    date = models.DateField(auto_now_add = False)
    time = models.TimeField(auto_now_add = False)
    price = models.FloatField()

    def __str__(self):
    	return "{} - {} - {} - {}".format(self.airline_name, self.date, self.time, self.price)

class Accommodation(models.Model):
    hotel_name = models.CharField(max_length = 256)
    price = models.FloatField()
    address = models.CharField(max_length = 256)
    image = models.ImageField(upload_to='home/media/accommodations/', max_length=255)
    
    def __str__(self):
        return "{} - {} - {} - {}".format(self.hotel_name, self.price, self.address, self.image)

class Attraction(models.Model):
    attraction_name = models.CharField(max_length = 256)
    price = models.FloatField()
    address = models.CharField(max_length = 256)
    image = models.ImageField(upload_to='home/media/attractions/', max_length=255)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.attraction_name, self.price, self.address, self.image)