from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>', views.add, name='add-to-cart'),
    # path('update_item/', views.updateItem, name="updateItem"),
    path('cart/i/<int:id>/', views.increaseQuantity, name="increase-quantity"),
    path('cart/d/<int:id>/', views.decreaseQuantity, name="decrease-quantity"),
    path('cart/remove/<int:id>/', views.remove_from_cart, name="remove-from-cart")

]
