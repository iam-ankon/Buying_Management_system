from rest_framework import generics
from .models import StatusOfInquiry
from .serializers import StatusOfInquirySerializer

# List and create inquiries
class StatusOfInquiryListCreateView(generics.ListCreateAPIView):
    queryset = StatusOfInquiry.objects.all()
    serializer_class = StatusOfInquirySerializer

# Retrieve, update, and delete a specific inquiry
class StatusOfInquiryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StatusOfInquiry.objects.all()
    serializer_class = StatusOfInquirySerializer

# Filtered view for confirmed inquiries
class ConfirmedInquiryListView(generics.ListAPIView):
    queryset = StatusOfInquiry.objects.filter(is_confirmed=True)
    serializer_class = StatusOfInquirySerializer

# Filtered view for pending inquiries
class PendingInquiryListView(generics.ListAPIView):
    queryset = StatusOfInquiry.objects.filter(is_confirmed=False)
    serializer_class = StatusOfInquirySerializer
