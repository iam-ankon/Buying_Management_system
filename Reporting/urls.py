from django.urls import path
from .views import (
    DailyProductionReportListCreateView,
    DailyProductionReportDetailView,
    MonthlyProductionReportListCreateView,
    MonthlyProductionReportDetailView,
    TotalOrderReportListCreateView,
    TotalOrderReportDetailView,
    EmployeeDatabaseReportListCreateView,
    EmployeeDatabaseReportDetailView,
    EmployeeAttendanceReportListCreateView,
    EmployeeAttendanceReportDetailView,
)

urlpatterns = [
    path('daily-production/', DailyProductionReportListCreateView.as_view(), name='daily-production-list-create'),
    path('daily-production/<int:pk>/', DailyProductionReportDetailView.as_view(), name='daily-production-detail'),
    path('monthly-production/', MonthlyProductionReportListCreateView.as_view(), name='monthly-production-list-create'),
    path('monthly-production/<int:pk>/', MonthlyProductionReportDetailView.as_view(), name='monthly-production-detail'),
    path('total-order/', TotalOrderReportListCreateView.as_view(), name='total-order-list-create'),
    path('total-order/<int:pk>/', TotalOrderReportDetailView.as_view(), name='total-order-detail'),
    path('employee-database/', EmployeeDatabaseReportListCreateView.as_view(), name='employee-database-list-create'),
    path('employee-database/<int:pk>/', EmployeeDatabaseReportDetailView.as_view(), name='employee-database-detail'),
    path('employee-attendance/', EmployeeAttendanceReportListCreateView.as_view(), name='employee-attendance-list-create'),
    path('employee-attendance/<int:pk>/', EmployeeAttendanceReportDetailView.as_view(), name='employee-attendance-detail'),
]
