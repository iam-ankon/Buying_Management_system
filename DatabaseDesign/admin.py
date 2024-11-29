from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'master_order_no', 
        'supplier_name', 
        'buyer_name', 
        'shipment_date', 
        'total_value', 
        'current_status'
    )
    list_filter = ('shipment_date', 'current_status', 'season_year', 'department')
    search_fields = ('master_order_no', 'supplier_name', 'buyer_name', 'order_no', 'ref_no', 'invoice_no')
    date_hierarchy = 'shipment_date'
    ordering = ('-shipment_date',)
