from django.contrib import admin
from .models import StatusOfInquiry

@admin.register(StatusOfInquiry)
class StatusOfInquiryAdmin(admin.ModelAdmin):
    list_display = ('inquiry_no', 'is_confirmed', 'description')
    search_fields = ('inquiry_no', 'description')
    list_filter = ('is_confirmed',)
    ordering = ('-is_confirmed', 'inquiry_no')
