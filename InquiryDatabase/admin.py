from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        'inquiry_no', 
        'buyer_name', 
        'supplier_name', 
        'request_qty', 
        'proposed_shipment_date'
    )
    search_fields = ('inquiry_no', 'buyer_name', 'supplier_name')
    list_filter = ('proposed_shipment_date', 'inquiry_received_date')
    date_hierarchy = 'proposed_shipment_date'
    ordering = ('-proposed_shipment_date',)
