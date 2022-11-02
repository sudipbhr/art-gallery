from store.models import Category
from store.models import OrderItem
from store.models import Order


def get_category(request):
    try:
        categories=Category.objects.all()
    except Category.DoesNotExist:
        categories= None
    return {
        'categories': categories,
    }

def items_count(request):
    if request.user.is_authenticated:
        order_no=Order.objects.filter(customer=request.user).first()
        items=OrderItem.objects.filter(order=order_no)
        count=items.count()
    else:
        count=0
    return{
        'count':count
    }

