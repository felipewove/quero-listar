from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Offer
from django.contrib.auth.models import User, Group


class OfferTests(APITestCase):
    def test_create_account_then_offer(self):
        url = reverse('user-list')
        data = {
            'username': 'DabApps'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'DabApps')
        response_offer = self.client.post(
            reverse('offer-list'),
            {
                'user': User.objects.first().id,
            },
            format='json'
        )
        self.assertEqual(response_offer.status_code, status.HTTP_201_CREATED)
