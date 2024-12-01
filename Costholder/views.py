# Costing/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import OwnCosting, SupplierCosting, Summary
from .serializers import OwnCostingSerializer, SupplierCostingSerializer, SummarySerializer

class OwnCostingListCreateView(ListCreateAPIView):
    queryset = OwnCosting.objects.all()
    serializer_class = OwnCostingSerializer

class SupplierCostingListCreateView(ListCreateAPIView):
    queryset = SupplierCosting.objects.all()
    serializer_class = SupplierCostingSerializer

class SummaryView(RetrieveAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

    def get_object(self):
        return Summary.objects.first()  # Assume only one summary entry
