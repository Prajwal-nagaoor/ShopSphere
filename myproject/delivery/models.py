from django.db import models

# Create your models here.
class Deliverymodel(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    customer_address = models.CharField(max_length=300)
    customer_mobile = models.IntegerField(max_length=13)