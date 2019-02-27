from django.db import models
from django.urls import reverse


# Create your models here.
class user_table(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)


class items_table(models.Model):

    p_id = models.CharField(max_length=20, default='p1')
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=100)
    category_choices = (
        ('Cameras and Photos', 'Cameras and Photos'),
        ('Computers and Laptops', 'Computers and Laptops'),
        ('Accessories', 'Accessories'),
        ('Smartphones and Tablets', 'Smartphones and Tablets'),
        ('TV and Audio', 'TV and Audio'),
        ('Video Games and Console', 'Video Games and Console'),
    )
    category = models.CharField(max_length=30, choices=category_choices)
    img = models.FileField(default='img')
    feature = models.BooleanField(default=False)
    discount = models.CharField(max_length=20,default=None)
    discountprice = models.CharField(max_length=20)


    #def get_absolute_url(self):
        #return reverse('items:detail1', kwargs={'pk': self.pk})

    def __str__(self):
        pid = self.p_id
        name = self.name
        price = self.price
        category = self.category
        return '{} - {} - {} - {}'.format(pid, name, price, category)


class CartTable(models.Model):
    uid = models.IntegerField()
    itemid = models.IntegerField()
    itemprice = models.IntegerField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        uid = self.uid
        itemid = self.itemid
        itemprice = self.itemprice
        quantity = self.quantity
        status = self.status
        return '{} - {} - {} - {} - {}'.format(uid, itemid, itemprice, quantity, status)


class CategoryTable(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        category_name = self.category_name
        return '{}'.format(category_name)

class Cart(models.Model):
    #items = models.ManyToManyField(CartItem, blank=True)
    total = models.DecimalField(decimal_places=2,max_digits=100,default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" %( self.id )


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True,)
    line_total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    item = models.ForeignKey(items_table,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.cart)






















