from rest_framework import serializers
from .models import Bitcoin
from django.db import models

class BitcoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitcoin
        #fields ="__all__"
        fields = ('id','name', 'price')

        read_only_fields = ('created_date', 'updated_date',)
