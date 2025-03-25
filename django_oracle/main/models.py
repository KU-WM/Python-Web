from django.db import models

class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'DJ_Customer'

    def __str__(self):
        return f"{self.id}: {self.name}"

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'DJ_Product'

    def __str__(self):
        return f"{self.id}: {self.name}"

class Order(models.Model):
    # id = models.IntegerField(primary_key=True,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DJ_Orders'
        
        
