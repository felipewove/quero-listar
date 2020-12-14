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


class QueroListarTests(APITestCase):
    def test_create_university_campus_course_offer(self):
        response_university = self.client.post(
            reverse("university-list"),
            {
                "name": "Anhembi",
                "score": 3.5,
                "logo_url": "https://logo.url/image.jpg",
            },
            format="json",
        )
        self.assertEqual(response_university.status_code, status.HTTP_201_CREATED)

        response_campus = self.client.post(
            reverse("campus-list"),
            {
                "name": "Name Of Campus",
                "city": "São José dos Campos",
                "university": response_university.data["id"],
            },
            format="json",
        )
        self.assertEqual(response_campus.status_code, status.HTTP_201_CREATED)

        response_course = self.client.post(
            reverse("course-list"),
            {
                "name": "Jornalismo",
                "kind": "Presencial",
                "level": "Bacharelado",
                "shift": "Noite",
                "campus": response_campus.data["id"],
            },
            format="json",
        )
        self.assertEqual(response_course.status_code, status.HTTP_201_CREATED)

        response_offer = self.client.post(
            reverse("offer-list"),
            {
                "full_price": 1227.05,
                "price_with_discount": 515.36,
                "discount_percentage": 58.01,
                "start_date": "01/08/2019",
                "enrollment_semester": "2019.2",
                "enabled": True,
                "course": response_course.data["id"],
            },
            format="json",
        )
        self.assertEqual(response_offer.status_code, status.HTTP_201_CREATED)
