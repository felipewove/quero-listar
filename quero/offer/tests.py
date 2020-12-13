from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import University


class UserTests(APITestCase):
    def test_create_account(self):
        url = reverse("user-list")
        data = {"username": "DabApps"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, "DabApps")


class UniversityTests(APITestCase):
    def test_create_account(self):
        response = self.client.post(
            reverse("university-list"),
            {
                "name": "Anhembi",
                "score": 3.5,
                "logo_url": "https://logo.url/image.jpg",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
