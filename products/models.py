from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='Images/')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
   

    def __str__(self):
        return self.name