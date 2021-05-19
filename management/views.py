
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth import get_user
from django.urls import reverse
# Create your views here.
from accounts.models import *
from core.models import *
from .forms import *



def admin_view(request):
    products=Product.objects.all()
    u=get_user(request)
    if u.is_staff:

        data={
            'products':products,
            'user':u,
            'status':True,
            'messege':None
        } 
        return render(request,'admin.html',context=data)
    else:
        return  redirect('core:home')  

def edit_view(request):
    u=get_user(request)
    products=Product.objects.all()
    imagelinklis={}
    for i in products:
        link=str(i.thumbnail)
        link=link.replace('manage','media')
        imagelinklis[i]=link
    if u.is_staff:
        data={
            'products':products,
            'imagelinklis':imagelinklis,
            'status':True,
            'messege':None
        }
        return render(request,'management/edit.html',data)
    else:
        return redirect('core:home') 

def edit_product(request,product_id):
    u=get_user(request)
    product=Product.objects.all().get(product_id=product_id)
    if u.is_staff:
        form=editform
        data={
            'status':True,
            'form':form,
            'messege':None,
            'product':product
        }
        return render(request,'management/product_edit.html',data)

def edit(request,product_id):
    u=get_user(request)
    product=Product.objects.all().get(product_id=product_id)
    if u.is_staff:
        if request.method=='POST':
            form=editform(request.POST,request.FILES)
            if form.is_valid():
                lis=['product_name','product_brand','product_type','product_description', 'product_price','product_price,thumbnail']
                for i in lis:
                    j=form.cleaned_data.get(i)
                    if j==None or j=='' or j==" ":
                        continue
                    elif i=='product_price':
                        product.product_price=j
                    elif i=='product_type':
                        product.product_type=j
                    elif i=='product_name':
                        product.product_name=j
                    elif i=='product_brand':
                        product.product_brand=j
                    elif i=='product_description':
                        product.product_price=j  
                    elif i=='thumbnail':
                        product.thumbnail=j  
                product.save()                    
                return redirect('management:edit_view')
                               
            else:
                return HttpResponse(u.username)
    return redirect('core:home')

def product_add(request):
    u=get_user(request)
    if u.is_staff:
        form=Productform
        data={
            'status':True,
            'form':form,
            'messege':None
        }
        return render(request,'management/add.html',data)
    else:
        return redirect('core:home')  
def add(request):
    u=get_user(request)
    if (u.is_staff):
        if request.method=='POST':
            form=Productform(request.POST,request.FILES)
            if form.is_valid():
                product_name=form.cleaned_data.get("product_name")
                product_brand=form.cleaned_data.get("product_brand")
                product_type=form.cleaned_data.get("product_type")
                product_description=form.cleaned_data.get("product_type")
                product_price=form.cleaned_data.get("product_price")
                thumbnail=form.cleaned_data.get("thumbnail")
                product=Product.objects.create(
                    product_name=product_name,
                    product_brand=product_brand,
                    product_type=product_type,
                    product_price=product_price,
                    product_description=product_description,
                    thumbnail=thumbnail
                    )
                product.save()    
                return redirect('management:manage')
            else:
                return redirect('core:home')
        else:
            return redirect('core:home')           
    else:
        return redirect('core:home')            


        