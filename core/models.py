from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """definition time stamp model"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        abstract = True