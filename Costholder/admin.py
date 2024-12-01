# Costing/admin.py
from django.contrib import admin
from .models import OwnCosting, SupplierCosting, Summary

@admin.register(OwnCosting)
class OwnCostingAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_cost', 'description')

@admin.register(SupplierCosting)
class SupplierCostingAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'material', 'cost')

@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('total_own_costing', 'total_supplier_costing')
