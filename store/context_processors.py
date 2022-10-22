from store.models import Category
from store.models import OrderItem
from store.models import Order

def get_category(request):
    categories=Category.objects.all()
    return {
        'categories': categories,
    }

def items_count(request):
    order_no=Order.objects.filter(customer=request.user.customer).first()
    items=OrderItem.objects.filter(order=order_no)
    count=items.count()

    return{
        'count':count
    }

