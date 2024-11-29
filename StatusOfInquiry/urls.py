from django.urls import path
from .views import (
    StatusOfInquiryListCreateView, 
    StatusOfInquiryDetailView,
    ConfirmedInquiryListView, 
    PendingInquiryListView
)

urlpatterns = [
    path('inquiries/', StatusOfInquiryListCreateView.as_view(), name='inquiry-list-create'),
    path('inquiries/<int:pk>/', StatusOfInquiryDetailView.as_view(), name='inquiry-detail'),
    path('inquiries/confirmed/', ConfirmedInquiryListView.as_view(), name='confirmed-inquiries'),
    path('inquiries/pending/', PendingInquiryListView.as_view(), name='pending-inquiries'),
]
