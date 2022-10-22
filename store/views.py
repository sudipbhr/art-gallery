from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .models import *

# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        items=[]
        order =''
    products= Product.objects.all()
    context={
        'products':products,
        }
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
        count= items.count()
    else:
        items=[]
        order =''
    context={
        'items':items,
        'order':order
        }
    return render(request,'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        items=[]
        order =''
    context={
        'items':items,
        'order':order
        }
    return render(request,'store/checkout.html', context)
    

def add(request, product_id):
    order_no = Order.objects.filter(customer=request.user.customer).first()
    p_id = get_object_or_404(Product, id=product_id)
    orderitem, created = OrderItem.objects.get_or_create(order = order_no, product = p_id)
    pre_quantity= orderitem.quantity
    new_quantity= pre_quantity+1
    orderitem.quantity= new_quantity
    orderitem.save()
    messages.success(request, "Item added to card successfully")
    return redirect('/cart/')

# def updateItem(request):
#     return JsonResponse("Item is added", safe=False)

def increaseQuantity(request, id):
    try:
        productExits = OrderItem.objects.get(id=id)
        pre_quantity = productExits.quantity
        new_quantity = pre_quantity + 1
        productExits.quantity=new_quantity
        productExits.save()
    except:
        messages.error(request, "Invalid Access")
    return redirect('/cart/')


def decreaseQuantity(request, id):
    try:
        productExits = OrderItem.objects.get(id=id)
        pre_quantity = productExits.quantity
        new_quantity = pre_quantity - 1
        productExits.quantity=new_quantity
        productExits.save()
    except:
        messages.error(request, "Invalid Access")
    return redirect('/cart/')

def remove_from_cart(request, id):
    order_no= Order.objects.filter(customer=request.user.customer).first()
    p_id = get_object_or_404(Product, id=id)
    order = OrderItem.objects.get(product=p_id, order=order_no)
    order.delete()
    messages.success(request,"Removed from the cart")
    return redirect('/cart/')


def page_not_found_view(request, exception):
    return render(request, 'store/404.html', status=404)