from django.urls import path
from .views import (
    SampleFollowUpListCreateView, SampleFollowUpDetailView,
    SampleCommentListCreateView, SampleCommentDetailView,
    ReminderListCreateView, ReminderDetailView
)

urlpatterns = [
    path('sample-follow-ups/', SampleFollowUpListCreateView.as_view(), name='sample-follow-up-list-create'),
    path('sample-follow-ups/<int:pk>/', SampleFollowUpDetailView.as_view(), name='sample-follow-up-detail'),
    path('sample-comments/', SampleCommentListCreateView.as_view(), name='sample-comment-list-create'),
    path('sample-comments/<int:pk>/', SampleCommentDetailView.as_view(), name='sample-comment-detail'),
    path('reminders/', ReminderListCreateView.as_view(), name='reminder-list-create'),
    path('reminders/<int:pk>/', ReminderDetailView.as_view(), name='reminder-detail'),
]
