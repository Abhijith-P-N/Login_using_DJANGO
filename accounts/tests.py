from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class RegistrationTestCase(TestCase):
    def test_registration_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)