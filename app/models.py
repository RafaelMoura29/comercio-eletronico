from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    img_url = models.CharField(max_length=400)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    product_fk= models.ManyToManyField(Product, blank = True)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.pk)