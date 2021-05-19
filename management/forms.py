
from django.forms import fields
from django import forms 
from .models import *
from accounts.models import *
from core.models import *


class Productform(forms.Form):
    product_name=forms.CharField(required=True)
    product_brand=forms.CharField(required=False)
    product_type=forms.CharField(required=False)
    product_description=forms.CharField(required=False)
    product_price=forms.IntegerField(required=True)
    thumbnail=forms.ImageField(required=False)

class editform(forms.Form):
    product_name=forms.CharField(required=False)
    product_brand=forms.CharField(required=False)
    product_type=forms.CharField(required=False)
    product_description=forms.CharField(required=False)
    product_price=forms.IntegerField(required=False)
    thumbnail=forms.ImageField(required=False)