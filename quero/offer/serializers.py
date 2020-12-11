from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Offer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'offer']
        read_only_fields = ['offer']
        depth = 1


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['url', ]