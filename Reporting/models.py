from django.db import models

class DailyProductionReport(models.Model):
    report_date = models.DateField()  # Date of production
    total_output = models.PositiveIntegerField()  # Total items produced
    defective_items = models.PositiveIntegerField(default=0)  # Defective items count
    remarks = models.TextField(null=True, blank=True)  # Additional comments

    def __str__(self):
        return f"Daily Production Report - {self.report_date}"


class MonthlyProductionReport(models.Model):
    month = models.CharField(max_length=20)  # Month and year (e.g., "November 2024")
    total_output = models.PositiveIntegerField()  # Total production for the month
    defective_items = models.PositiveIntegerField(default=0)  # Total defective items
    remarks = models.TextField(null=True, blank=True)  # Additional comments

    def __str__(self):
        return f"Monthly Production Report - {self.month}"


class TotalOrderReport(models.Model):
    order_id = models.CharField(max_length=255, unique=True)  # Unique order ID
    customer_name = models.CharField(max_length=255)  # Customer placing the order
    total_items = models.PositiveIntegerField()  # Total items in the order
    order_date = models.DateField()  # Date of order
    status = models.CharField(max_length=100)  # Order status (e.g., "Completed", "Pending")

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"


class EmployeeDatabaseReport(models.Model):
    employee_id = models.CharField(max_length=255, unique=True)  # Employee ID
    name = models.CharField(max_length=255)  # Employee Name
    department = models.CharField(max_length=255)  # Department
    join_date = models.DateField()  # Date of joining
    active_status = models.BooleanField(default=True)  # Is the employee currently active?

    def __str__(self):
        return f"Employee {self.name} - {self.department}"


class EmployeeAttendanceReport(models.Model):
    employee = models.ForeignKey(EmployeeDatabaseReport, on_delete=models.CASCADE)  # Linked to Employee Database
    date = models.DateField()  # Attendance date
    status = models.CharField(max_length=50, choices=[('Present', 'Present'), ('Absent', 'Absent')])  # Attendance status
    remarks = models.TextField(null=True, blank=True)  # Additional remarks

    def __str__(self):
        return f"{self.employee.name} - {self.date} ({self.status})"
