from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quero.offer.serializers import UserSerializer, GroupSerializer, OfferSerializer	
from quero.offer.models import Offer


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
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
