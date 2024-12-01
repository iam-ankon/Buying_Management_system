from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'position', 'join_date', 'active_status')
    search_fields = ('employee_id', 'name', 'department', 'position')
    list_filter = ('department', 'active_status')
    ordering = ('-join_date',)
