from rest_framework import generics
from .models import Inquiry
from .serializers import InquirySerializer

class InquiryListCreateView(generics.ListCreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

class InquiryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
