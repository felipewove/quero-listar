from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Offer, Course, Campus, University


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
        depth = 1


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        depth = 3
        fields = ['id', 'full_price', 'price_with_discount', 'start_date', 'enrollment_semester', 'enabled', 'course']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        depth = 2
        fields = '__all__'


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        depth = 1
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
