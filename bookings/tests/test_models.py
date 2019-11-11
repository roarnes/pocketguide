from bookings.models import User, Booking
from django.test import TestCase
from django.utils import timezone
from faker import Faker

faker = Faker()

class TestModels(TestCase):

    def create_User(self):
        return User.objects.create(first_name = faker.first_name(), surename = faker.last_name())

    def create_Booking(self):
        return Booking.objects.create(
            name = faker.first_name(),
            type = faker.random.randint(1,3),
            time_begin = timezone.now(),
            time_end = timezone.now() + timezone.timedelta(days=faker.random.randint(1,10)),
            location = faker.address(),
            user = User.objects.get(id=faker.random.randint(1,5))
        )

    def test_user_creation(self):
        user = self.create_User()
        self.assertTrue(isinstance(user, User))

    def test_Booking_creation(self):
        booking = self.create_Booking()
        self.assertTrue(isinstance(booking,Booking))