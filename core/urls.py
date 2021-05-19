from django.urls import path, include
from .views import *

app_name='core'
urlpatterns=[
    path('core',home,name="home"),
    path('loginpage',login_view,name="login_view"),
    path('sighnup',sighnup,name="sighnup"),
    path('addtocart',addtocart,name="addtocart"),
    path('cart',cart,name='cart'),  
    path('<int:product_id>/',product_view,name="product_view"),
    path('buy/<int:cart_id>/',buy,name="buy"),
    path('order/<int:cart_id>/',buy_view,name="buy_view"),
    path('removeitem',removefromcart,name="remove"),
]