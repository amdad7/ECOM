
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import Transaction
from django.contrib.auth import get_user
from ECOM import settings
from accounts.models import *
from core.models import *
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt
razorpay_id="rzp_test_VpHf61FjQtCo1B"
razorpay_account_id="mTc7KLspms1dhU7ASKfnTmne"
razor_client=razorpay.Client(auth={razorpay_id,razorpay_account_id})
# Create your views here.





@login_required
def payment(request,order_id):
    u=get_user(request)
    _order=Order.objects.all().get(order_id=order_id)

    #callback_url='http://'
    order_currency='INR'
    notes={'order-type':"basic produt order"}
    data={
        'amount':_order.total_price*100,
        'currency':order_currency,
        #'reciept':_order.order_id,
        'payment_capture':1

    }
    razor_client=razorpay.Client(auth=(razorpay_id,razorpay_account_id))
    razorpay_order=razor_client.order.create(data)
    data_id=razorpay_order['id']
    transaction=Transaction(order=_order,data_id=data_id)
    print(data_id)
    context={
        'order':_order,
        'amount':_order.total_price*100,
        'currency':order_currency,
        'reciept':_order.order_id,
        'user':u,
        'data_order_id':data_id,
        'razorpay_id':razorpay_id
    }
    return render(request,'razorpay/payment.html',context)


@csrf_exempt
@login_required
def paymencallback(request):
    if request.method=='POST':
        payment_id=request.POST.get('razorpay_payment_id')
        signature=request.POST.get('razorpay_signature')
        rorder_id=request.POST.get('razorpay_signature')
        client = razorpay.Client(auth = (razorpay_id, razorpay_account_id))
        params_dict = {
            'rorder_id': '12122',
            'payment_id': '332',
            'signature': '23233'
        }
        client.utility.verify_payment_signature(params_dict)
        return render(request,'razorpay/success.html')

    else:
        return JsonResponse({'status':'denied'})    