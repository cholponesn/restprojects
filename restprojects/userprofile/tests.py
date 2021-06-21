from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class RegisterTest(APITestCase):

    def setUp(self):
        self.url = reverse('register')

    def test_register_ok(self):
        data = {
            "username":"maksimka1234",
            "password":"123456",
            "check_password":"123456",
            "profile":{
            "full_name":"maksimka"
            }
        }
        self.response = self.client.post(self.url,data,format="json")
        self.assertEqual(self.response.status_code,201)
