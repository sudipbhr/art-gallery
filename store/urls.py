from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product/detail/<int:id>/', views.product_detail, name="product-detail"),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    # category view pages
    path('category/<str:cat_name>/', views.categoryView, name="category-view"),
    # search urls
    path('search/', views.search, name='search'),
    path('cart/add/<int:product_id>/', views.add, name='add-to-cart'),
    # path('update_item/', views.updateItem, name="updateItem"),
    path('cart/i/<int:id>/', views.increaseQuantity, name="increase-quantity"),
    path('cart/d/<int:id>/', views.decreaseQuantity, name="decrease-quantity"),
    path('cart/remove/<int:id>/', views.remove_from_cart, name="remove-from-cart"),
    path('checkout/process_trans/', views.process_trans, name="process_trans"),

]
