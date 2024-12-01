from django.db import models
from Reporting.models import DailyProductionReport  # Import the Reporting table

class Employee(models.Model):
    employee_id = models.CharField(max_length=255, unique=True)  # Unique Employee ID
    name = models.CharField(max_length=255)  # Employee Name
    department = models.CharField(max_length=255)  # Department
    position = models.CharField(max_length=255)  # Job position
    join_date = models.DateField()  # Joining date
    active_status = models.BooleanField(default=True)  # Active or inactive employee
    daily_report = models.ForeignKey(DailyProductionReport, on_delete=models.CASCADE, related_name="employees")  # Linked to Reporting table

    def __str__(self):
        return f"{self.name} - {self.position} ({self.employee_id})"
