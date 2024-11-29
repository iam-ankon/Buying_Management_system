from django.contrib import admin
from .models import Inquiry, TotalInquiry

class TotalInquiryAdmin(admin.ModelAdmin):
    list_display = ('inquiry', 'added_at')  # Fields to display in the list view
    search_fields = ('inquiry__inquiry_no',)  # Enable search by inquiry number
    list_filter = ('added_at',)  # Add filter by timestamp

# Registering the TotalInquiry model
admin.site.register(TotalInquiry, TotalInquiryAdmin)

