from django.db import models
from InquiryDatabase.models import Inquiry  # Import the Inquiry model from InquiryDatabase app


class TotalInquiry(models.Model):
    inquiry = models.OneToOneField(
        Inquiry,
        on_delete=models.CASCADE,
        to_field="inquiry_no",  # Connect using 'inquiry_no'
        related_name="total_inquiry"
    )  # One-to-One relationship
    added_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the inquiry was added

    def __str__(self):
        return f"Total Inquiry for {self.inquiry.inquiry_no}"