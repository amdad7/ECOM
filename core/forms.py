from django.db.models.query_utils import PathInfo
from django.forms import fields
from django import forms 

class dataform(forms.Form):
    address=forms.CharField(max_length=200,required=True)
    phone_no=forms.CharField(max_length=20,required=True)
    zip_code=forms.IntegerField(required=True)
    