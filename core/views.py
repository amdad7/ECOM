
from .models import *
from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth import get_user
from django.urls import reverse
from accounts.models import User
from accounts.forms import RegistrationForm
from .forms import *
# Create your views here.
def login_view(request):
    return render(request,'reglog/login.html')
def sighnup(request):
    form=RegistrationForm
    return render(request,'reglog/sighnup.html',context={'form':form})

def home(request):
    products=Product.objects.all()
    u=get_user(request)
    try:
        user=User.objects.all().get(email=u)
        try:
            cart=Cart.objects.all().get(cart_user=u)
        except:
            cart=Cart(cart_user=u) 
            cart.save()   
        status=True
    except:
        user="not_logged_in"
        cart=None
        status=False    
    data={
        'products':products,
        'cart':cart,
        'user':user,
        'status':status,
        'messege':'',
    }
    return render(request,'home.html',context=data)

def product_view(request,product_id):
    product=Product.objects.all().get(product_id=product_id)
    data={
        'product_name':product.product_name,
        'product_brand':product.product_brand,
        'product_type':product.product_type,
        'product_description':product.product_description,
        'product_price':product.product_price 
    }
    return JsonResponse(data)

 

def addtocart(request):
    if request.method=='POST':
        try:           
            u=get_user(request)
            user=User.objects.all().get(email=u)
            cart=Cart.objects.all().get(User=user)
            product_id=request.POST.get('product_id')
            product=Product.objects.all().get(product_id=product_id)
            quantity=request.POST.get('quantity')
            item=Item(product=product,quantity=quantity,user=user)
            item.save()
            cart.items.add(item)
            cart.total_price+=product.product_price
            cart.save()
            data={
                'status':'addedtocart',
                'error':None
            }
            
        except:
            data={
                'status':'error',
                'error':'user not logged in'
            }    
        return JsonResponse(data) 
    else:
        return redirect('home')     

def removefromcart(request):
    pass

def cart(request):
    u=get_user(request)
    try:
        user=User.objects.all().get(email=u)
        cart=Cart.objects.all().get(cart_user=u)
        amount=0        
        for item in cart.items.all():
            amount+=(float(item.product.product_price)*int(item.quantity))
        cart.total_price=int(amount)
        cart.save()    
    except:
        return redirect('core:home') 
    data={
        'cart':cart,
        'user':user,
        'status':True,
    }
    return render(request,'cart.html',context=data)     

def buy_view(request,cart_id):
    form=dataform
    u=get_user(request)
    try:
        user=User.objects.all().get(email=u)
        cart=Cart.objects.all().get(cart_user=u)
    except:
        return redirect('core:home') 
    data={
        'form':form,
        'cart':cart,
    }    
    return render(request,'buy_view.html',data)

def buy(request,cart_id):
    if request.method=="POST":
        u=get_user(request)
        user=User.objects.all().get(email=u)
        cart=Cart.objects.all().get(cart_user=u)
        order=Order()
        order.address=request.POST.get('address')
        order.phone_no=request.POST.get('phone_no')
        order.save()       
        for item in cart.items.all():
            order.items.add(item.product)
        order.total_price=cart.total_price
        order.save()    
        return render(request,'pay.html',context={'order':order})
    else:
       return redirect('home')    



   