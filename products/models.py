from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=225)
    stock=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


