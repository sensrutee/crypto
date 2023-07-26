from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from rest_framework import serializers
# Create your models here.



class Bitcoin(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

