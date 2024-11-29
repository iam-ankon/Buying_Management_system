from django.db import models

class Inquiry(models.Model):
    inquiry_no = models.CharField(max_length=255, unique=True)  # Inquiry or Request Number
    request_qty = models.PositiveIntegerField()  # Quantity requested
    proposed_shipment_date = models.DateField()  # Proposed shipment date
    inquiry_received_date = models.DateField()  # Date inquiry was received
    buyer_name = models.CharField(max_length=255)  # Buyer's name
    supplier_name = models.CharField(max_length=255)  # Supplier's name
    proposed_supplier_name = models.CharField(max_length=255, null=True, blank=True)  # Proposed supplier
    fob_in_pcs = models.DecimalField(max_digits=10, decimal_places=2)  # FOB price per piece
    fob_in_dz = models.DecimalField(max_digits=10, decimal_places=2)  # FOB price per dozen
    fabric_1_unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of fabric 1
    fabric_2_unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Price of fabric 2
    fabric_3_unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Price of fabric 3
    total_accessories_price = models.DecimalField(max_digits=10, decimal_places=2)  # Accessories price
    consumption = models.DecimalField(max_digits=10, decimal_places=2)  # Consumption cost
    print_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Printing cost
    wash_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Washing cost
    emb_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Embroidery cost
    others_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Other costs
    commission = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Commission
    commercial_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Commercial cost
    test_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Testing cost
    zipper_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Zipper cost
    thread_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Thread cost
    label_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Label cost
    hangtag_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Hangtag cost
    care_label_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Care label cost
    addition_label_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Additional label cost
    button_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Button cost

    def __str__(self):
        return f"Inquiry {self.inquiry_no} - {self.buyer_name}"
