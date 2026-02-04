from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Product(models.Model):
    CONDITION_CHOICES=[
        ('Like New','Like New'),
        ('Good','Good'),
        ('Used','Used'),
    ]
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    condition=models.CharField(max_length=20,choices=CONDITION_CHOICES)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='products/')    
    description=models.TextField()
    is_approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name