from django.db import models

class StatusOfInquiry(models.Model):
    inquiry_no = models.CharField(max_length=255, unique=True)  # Inquiry number
    description = models.TextField(null=True, blank=True)  # Description of the inquiry
    is_confirmed = models.BooleanField(default=False)  # Status: True = Confirmed, False = Pending

    def __str__(self):
        return f"Inquiry {self.inquiry_no} - {'Confirmed' if self.is_confirmed else 'Pending'}"
