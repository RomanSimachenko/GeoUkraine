from operator import mod
from django.contrib import admin
from . import models

admin.site.register(models.Universities)

admin.site.register(models.Regions)
