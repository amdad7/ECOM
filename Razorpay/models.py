
from django.db import models
import razorpay
from razorpay.resources import order
from accounts.models import *
from core.models import *
# Create your models here.
class Transaction(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    data_id=models.CharField(max_length=100,default=None)
    payment_id=models.CharField(max_length=100,default=None)
    rorder_id=models.CharField(max_length=100,default=None)
    signature=models.CharField(max_length=100,default=None)