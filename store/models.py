from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Category(models.Model):
    cat_name=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.cat_name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name=models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    price=models.FloatField()
    digital =models.BooleanField(default=False, null=True, blank=False)
    image=models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    customer=models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transcation_id= models.CharField(default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)

    def __str__(self):
        return str(self.id)

    @property
    # find total number of items
    def get_total(self):
        orderitem= self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total
    
    def get_cart_total(self):
        orderitem= self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return total

class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.IntegerField(default=0)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address=models.CharField(max_length=200, null=True)
    city=models.CharField(max_length=200, null=True)
    state=models.CharField(max_length=200, null=True)
    zipcode=models.IntegerField(null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "Shipping Address"


