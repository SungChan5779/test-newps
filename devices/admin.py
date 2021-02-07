from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Device)
class Devices(admin.ModelAdmin):
    pass