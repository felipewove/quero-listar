from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quero.offer.serializers import UserSerializer, GroupSerializer, OfferSerializer, CourseSerializer, CampusSerializer, UniversitySerializer

from .models import Offer, Course, Campus, University


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CampusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campi to be viewed or edited.
    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Universities to be viewed or edited.
    """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
