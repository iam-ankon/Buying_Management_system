from rest_framework import serializers
from .models import TotalInquiry
from InquiryDatabase.models import Inquiry

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'

class TotalInquirySerializer(serializers.ModelSerializer):
    inquiry_details = InquirySerializer(source='inquiry', read_only=True)

    class Meta:
        model = TotalInquiry
        fields = ['id', 'inquiry', 'inquiry_details', 'added_at']
