import uuid

from django.db import models
from django.conf import settings


class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
