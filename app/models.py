from django.db import models


class CustomerDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.price
