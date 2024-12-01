# Costing/serializers.py
from rest_framework import serializers
from .models import OwnCosting, SupplierCosting, Summary

class OwnCostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnCosting
        fields = '__all__'

class SupplierCostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierCosting
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'
