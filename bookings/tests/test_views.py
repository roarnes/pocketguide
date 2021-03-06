from django.test import TestCase, RequestFactory
from django.urls import reverse
from bookings.views import index

class TestViews(TestCase):

    def test_index(self):
        path = reverse('bookings:index', kwargs={'user_id': 1})
        request = RequestFactory().get(path)
        
        response = index(request, 1)
        assert response.status_code == 200