from django.contrib.auth.models import Group, User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Campus, Course, Offer, University
from .serializers import (CampusSerializer, CourseSerializer, GroupSerializer,
                          OfferSerializer, UniversitySerializer,
                          UserSerializer)


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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "course__name",
        "course__kind",
        "course__level",
        "course__shift",
        "course__campus__city",
        "course__campus__university__name",
    ]
    ordering_fields = ['discount_percentage']


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['kind', 'level', 'shift', 'campus__university__name']


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
