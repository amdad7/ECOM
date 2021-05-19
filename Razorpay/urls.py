from django.urls import path, include
from .views import *

app_name='Razorpay'
urlpatterns=[
   path('razorpay/<int:order_id>/',payment,name="payment")
]