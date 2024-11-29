from django.urls import path
from .views import TotalInquiryListCreateView, TotalInquiryDetailView

urlpatterns = [
    path('total-inquiries/', TotalInquiryListCreateView.as_view(), name='total-inquiry-list-create'),
    path('total-inquiries/<int:pk>/', TotalInquiryDetailView.as_view(), name='total-inquiry-detail'),
]
