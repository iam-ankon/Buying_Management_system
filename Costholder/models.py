# Costing/models.py
from django.db import models

class OwnCosting(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class SupplierCosting(models.Model):
    supplier_name = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.supplier_name} - {self.material}"

class Summary(models.Model):
    total_own_costing = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_supplier_costing = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "Costing Summary"
