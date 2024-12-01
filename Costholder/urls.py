# Costing/urls.py
from django.urls import path
from .views import OwnCostingListCreateView, SupplierCostingListCreateView, SummaryView

urlpatterns = [
    path('own-costing/', OwnCostingListCreateView.as_view(), name='own-costing'),
    path('supplier-costing/', SupplierCostingListCreateView.as_view(), name='supplier-costing'),
    path('summary/', SummaryView.as_view(), name='summary'),
]
