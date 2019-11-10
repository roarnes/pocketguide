from django.test import TestCase
from .models import Flight, Accommodation, Attraction
from django.utils import timezone
from django.utils.timezone import datetime

# Create your tests here.
class ModelsTest(TestCase):
    @classmethod

    def create_flight(self, airline_name = "Garuda", from_city = "Jakarta", to_city = "Bali", price = "1999000"):
        return Flight.objects.create(airline_name=airline_name, date=datetime.today(), time=timezone.now(), from_city=from_city, to_city=to_city, price=price)

    def test_flight_creation(self):
        flight = self.create_flight()
        self.assertTrue(isinstance(flight, Flight))
        self.assertEqual(flight.__str__(), "{} - {} - {} - {}".format(flight.airline_name, flight.date, flight.time, flight.price))

    def create_accommodation(self, hotel_name = "Tentrem", price = "1299000", address = "Monjali, Jogja", image = "/home/media/accommodations/hotel1.jpg"):
        return Accommodation.objects.create(hotel_name = hotel_name, price = price, address = address, image = image)

    def test_accommodation_creation(self):
        acc = self.create_accommodation()
        self.assertTrue(isinstance(acc, Accommodation))
        self.assertEqual(acc.__str__(), "{} - {} - {} - {}".format(acc.hotel_name, acc.price, acc.address, acc.image))

    def create_attraction(self, attraction_name = "Ubud Monkey Forest", price = "50000", address = "Ubud, Bali", image = "/home/media/attractions/attraction3.jpg"):
        return Attraction.objects.create( attraction_name = attraction_name, price = price, address = address, image = image)

    def test_attraction_creation(self):
        attr = self.create_attraction()
        self.assertTrue(isinstance(attr, Attraction))
        self.assertEqual(attr.__str__(), "{} - {} - {} - {}".format(attr.attraction_name, attr.price, attr.address, attr.image))

class BaseViewTest(TestCase):
	@classmethod
	
    def test_attraction_creation(self):
        attr = self.create_attraction()
        self.assertTrue(isinstance(attr, Attraction))
        self.assertEqual(attr.__str__(), "{} - {} - {} - {}".format(attr.attraction_name, attr.price, attr.address, attr.image))
