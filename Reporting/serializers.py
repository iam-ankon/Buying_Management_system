from rest_framework import serializers
from .models import (
    DailyProductionReport,
    MonthlyProductionReport,
    TotalOrderReport,
    EmployeeDatabaseReport,
    EmployeeAttendanceReport,
)

class DailyProductionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyProductionReport
        fields = '__all__'


class MonthlyProductionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyProductionReport
        fields = '__all__'


class TotalOrderReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalOrderReport
        fields = '__all__'


class EmployeeDatabaseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDatabaseReport
        fields = '__all__'


class EmployeeAttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAttendanceReport
        fields = '__all__'
