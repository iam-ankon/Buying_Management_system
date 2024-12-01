from rest_framework import generics
from .models import (
    DailyProductionReport,
    MonthlyProductionReport,
    TotalOrderReport,
    EmployeeDatabaseReport,
    EmployeeAttendanceReport,
)
from .serializers import (
    DailyProductionReportSerializer,
    MonthlyProductionReportSerializer,
    TotalOrderReportSerializer,
    EmployeeDatabaseReportSerializer,
    EmployeeAttendanceReportSerializer,
)

# Daily Production Report Views
class DailyProductionReportListCreateView(generics.ListCreateAPIView):
    queryset = DailyProductionReport.objects.all()
    serializer_class = DailyProductionReportSerializer


class DailyProductionReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyProductionReport.objects.all()
    serializer_class = DailyProductionReportSerializer


# Monthly Production Report Views
class MonthlyProductionReportListCreateView(generics.ListCreateAPIView):
    queryset = MonthlyProductionReport.objects.all()
    serializer_class = MonthlyProductionReportSerializer


class MonthlyProductionReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonthlyProductionReport.objects.all()
    serializer_class = MonthlyProductionReportSerializer


# Total Order Report Views
class TotalOrderReportListCreateView(generics.ListCreateAPIView):
    queryset = TotalOrderReport.objects.all()
    serializer_class = TotalOrderReportSerializer


class TotalOrderReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TotalOrderReport.objects.all()
    serializer_class = TotalOrderReportSerializer


# Employee Database Report Views
class EmployeeDatabaseReportListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeDatabaseReport.objects.all()
    serializer_class = EmployeeDatabaseReportSerializer


class EmployeeDatabaseReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeDatabaseReport.objects.all()
    serializer_class = EmployeeDatabaseReportSerializer


# Employee Attendance Report Views
class EmployeeAttendanceReportListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeAttendanceReport.objects.all()
    serializer_class = EmployeeAttendanceReportSerializer


class EmployeeAttendanceReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeAttendanceReport.objects.all()
    serializer_class = EmployeeAttendanceReportSerializer
