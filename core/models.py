from django.db import models
from time import time
import uuid
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL
from django.db.models.fields.related import ForeignKey, ManyToManyField
from accounts.models import User
from accounts.forms import *
# Create your models here.

def upload_path_handler(instance,filename):
    return 'thumbnails/{0}/{1}'.format(instance.product_id,filename)

class Product(models.Model):
    #product_id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4())
    #product_uploadedby=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.AutoField(primary_key=True,unique=True,auto_created=True)
    product_name=models.CharField(max_length=50)
    product_brand=models.CharField(max_length=50)
    product_type=models.CharField(max_length=50)
    product_description=models.TextField(max_length=500)
    product_price=models.IntegerField(default=0)
    thumbnail=models.ImageField(upload_to=upload_path_handler,blank=False)

    def __str__(self):
        return self.product_name

class Item(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=CASCADE)
    quantity=models.IntegerField(default=1)
    class Meta:
        unique_together=[['user','product']]

class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True,unique=True,auto_created=True)
    cart_user=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Item)
    total_price=models.IntegerField(default=0)
    def __str__(self):
        return self.cart_user.username

class Order(models.Model):
    order_id=models.AutoField(primary_key=True,unique=True,auto_created=True)
    items=models.ManyToManyField(Product)
    address=models.TextField(max_length=500)
    phone_no=models.IntegerField()
    total_price=models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.order_id)