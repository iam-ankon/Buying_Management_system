from rest_framework import generics
from .models import SampleFollowUp, SampleComment, Reminder
from .serializers import SampleFollowUpSerializer, SampleCommentSerializer, ReminderSerializer

class SampleFollowUpListCreateView(generics.ListCreateAPIView):
    queryset = SampleFollowUp.objects.all()
    serializer_class = SampleFollowUpSerializer

class SampleFollowUpDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SampleFollowUp.objects.all()
    serializer_class = SampleFollowUpSerializer

class SampleCommentListCreateView(generics.ListCreateAPIView):
    queryset = SampleComment.objects.all()
    serializer_class = SampleCommentSerializer

class SampleCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SampleComment.objects.all()
    serializer_class = SampleCommentSerializer

class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
