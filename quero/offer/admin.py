from django.contrib import admin

from . import models


admin.site.register(models.Offer)
admin.site.register(models.Course)
admin.site.register(models.Campus)
admin.site.register(models.University)
