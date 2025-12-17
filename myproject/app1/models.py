from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name
class productsmodel(models.Model):
    product_category=models.ForeignKey(category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=100)
    product_price=models.IntegerField(default=0)
    product_image=models.ImageField(default='default.png',upload_to='uploads')          
    trending = models.BooleanField(default=0)
    offer = models.BooleanField(default=0)
class cartmodel(models.Model):
    product_category = models. CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=100)
    product_price=models.IntegerField(default=0)
    product_image=models.ImageField(default='default.png',upload_to='uploads')  
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    
