from django.contrib import admin
from .models import (
    DailyProductionReport,
    MonthlyProductionReport,
    TotalOrderReport,
    EmployeeDatabaseReport,
    EmployeeAttendanceReport,
)

@admin.register(DailyProductionReport)
class DailyProductionReportAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'total_output', 'defective_items')
    search_fields = ('report_date',)


@admin.register(MonthlyProductionReport)
class MonthlyProductionReportAdmin(admin.ModelAdmin):
    list_display = ('month', 'total_output', 'defective_items')
    search_fields = ('month',)


@admin.register(TotalOrderReport)
class TotalOrderReportAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'total_items', 'order_date', 'status')
    search_fields = ('order_id', 'customer_name')


@admin.register(EmployeeDatabaseReport)
class EmployeeDatabaseReportAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'join_date', 'active_status')
    search_fields = ('employee_id', 'name', 'department')


@admin.register(EmployeeAttendanceReport)
class EmployeeAttendanceReportAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    search_fields = ('employee__name', 'date')
