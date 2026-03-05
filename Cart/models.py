from django.db import models

from products.models import Product


class Cart(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    
    