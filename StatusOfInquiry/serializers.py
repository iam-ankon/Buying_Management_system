from rest_framework import serializers
from .models import StatusOfInquiry

class StatusOfInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOfInquiry
        fields = '__all__'
