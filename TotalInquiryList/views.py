from rest_framework import generics
from .models import TotalInquiry
from .serializers import TotalInquirySerializer

# List all total inquiries and create a new one
class TotalInquiryListCreateView(generics.ListCreateAPIView):
    queryset = TotalInquiry.objects.all()
    serializer_class = TotalInquirySerializer

# Retrieve, update, and delete a specific total inquiry
class TotalInquiryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TotalInquiry.objects.all()
    serializer_class = TotalInquirySerializer
