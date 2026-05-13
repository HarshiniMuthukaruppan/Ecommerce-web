from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    STATUS_CHOISE=[
        ('pending','pending'),
        ('confirmed','confimed'),
        ('shipped','shipped'),
        ('delivered','delivered'),
        ('cancelled','cancelled'),
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    status=models.CharField(max_length=50, choices=STATUS_CHOISE,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return r"orders {self.id} by {self.user.username}"

class  OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return r"{self.quantity} x {self.product.name}"
