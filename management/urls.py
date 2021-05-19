from django.urls import path, include
from .views import *

app_name='management'
urlpatterns=[
    path('manage',admin_view,name="manage"),
    path('manage/editproducts',edit_view,name="edit_view"),
    path('manage/<int:product_id>/',edit_product,name="edit_product"),
    path('manage/addproducts',product_add,name="add_view"),
    path('edit/<int:product_id>/',edit,name="edit"),
    path('manage/addproducts/add',add,name="add")
]