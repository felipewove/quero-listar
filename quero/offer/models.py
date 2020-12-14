import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Offer(models.Model):
    """docstring for Offer"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_price = models.FloatField(_("Full Price"))
    price_with_discount = models.FloatField(_("Price With Discount"))
    discount_percentage = models.FloatField(_("Discount Percentage"))
    start_date = models.CharField(_("Stard Date"), max_length=10)
    enrollment_semester = models.CharField(_("Enrollment Semester"), max_length=6)
    enabled = models.BooleanField(default=False)
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING)


class Course(models.Model):
    """docstring for Course"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255)
    kind = models.CharField(_("Kind"), max_length=255)
    level = models.CharField(_("Level"), max_length=255)
    shift = models.CharField(_("Shift"), max_length=255)
    campus = models.ForeignKey('Campus', on_delete=models.DO_NOTHING)


class Campus(models.Model):
    """docstring for Campus"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255)
    city = models.CharField(_("City"), max_length=255)
    university = models.ForeignKey('University', on_delete=models.DO_NOTHING)


class University(models.Model):
    """docstring for University"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Company"), max_length=255)
    score = models.FloatField(_("Score"))
    logo_url = models.CharField(_("Logo"), max_length=255)
