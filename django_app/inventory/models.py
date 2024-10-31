from django.db import models


class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


class Material(models.Model):
    material_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.material_name


class Delivery(models.Model):
    delivery_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    delivery_days = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        # return f"Delivery {self.delivery_date} from {self.supplier}"
        return "Delivery"
