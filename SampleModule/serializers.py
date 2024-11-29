from rest_framework import serializers
from .models import SampleFollowUp, SampleComment, Reminder

class SampleFollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleFollowUp
        fields = '__all__'

class SampleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleComment
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
