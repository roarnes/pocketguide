from ptgride.models import PtgBooking, Location
from bookings.models import User
from django.test import TestCase
from django.utils import timezone
from faker import Faker

faker = Faker()

class TestModels(TestCase):

    def create_Location(self):
            return Location.objects.create(
                name='A',
                location=faker.random.randint(1,3)
            )

    def create_PtgBooking(self):
        return PtgBooking.objects.create(
            type = faker.random.randint(1,2),
            time_begin = timezone.now(),
            time_end = timezone.now() + timezone.timedelta(days=faker.random.randint(1,10)),
            pickup_location = Location.objects.get(pk=2),
            dropoff_location = Location.objects.get(pk=2),
            cost = faker.random.randint(1,100000),
            user = User.objects.get(id=faker.random.randint(1,5))
        )

    def test_location_creation(self):
        location = self.create_Location()
        self.assertTrue(isinstance(location, Location))

    def test_ptgBooking_creation(self):
        location = self.create_Location()
        ptgBooking = self.create_PtgBooking()
        self.assertTrue(isinstance(ptgBooking,PtgBooking))