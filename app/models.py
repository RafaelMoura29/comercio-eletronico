from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    img_url = models.CharField(max_length=400)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    