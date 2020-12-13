from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Campus, Course, Offer, University


class UserSerializer(serializers.ModelSerializer):

    """ Serialization of User model to render as JSON.
    The depth is responsible to render/show information of foreign key
    """
    
    class Meta:

        model = User
        fields = ["id", "username", "email", "groups"]
        depth = 1


class GroupSerializer(serializers.ModelSerializer):

    """ Serialization of Group model to render as JSON.
    """
    
    class Meta:

        model = Group
        fields = ["id", "name"]


class OfferSerializer(serializers.ModelSerializer):

    """ Serialization of Offer model to render as JSON.
    The depth is responsible to render/show information of foreign key
    """
    
    class Meta:

        model = Offer
        depth = 3
        fields = [
            "id",
            "full_price",
            "price_with_discount",
            "start_date",
            "enrollment_semester",
            "enabled",
            "course",
        ]


class CourseSerializer(serializers.ModelSerializer):

    """ Serialization of Course model to render as JSON.
    The depth is responsible to render/show information of foreign key
    """
    
    class Meta:
        
        model = Course
        depth = 2
        fields = "__all__"


class CampusSerializer(serializers.ModelSerializer):

    """ Serialization of Campus model to render as JSON.
    The depth is responsible to render/show information of foreign key
    """
    
    class Meta:

        model = Campus
        depth = 1
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):

    """ Serialization of University model to render as JSON.
    """
    
    class Meta:
        
        model = University
        fields = "__all__"
